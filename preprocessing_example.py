import cv2
import numpy as np

# Load image
img = cv2.imread("your_image.jpg")

# 1. Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Denoise (optional, helps with scans or noise)
denoised = cv2.fastNlMeansDenoising(gray, h=30)

# 3. Thresholding (Binarize)
# You can try cv2.THRESH_BINARY or cv2.ADAPTIVE_THRESH_GAUSSIAN_C
thresh = cv2.adaptiveThreshold(
    denoised, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 2
)

# 4. Invert if needed (OCR often expects black text on white)
inverted = cv2.bitwise_not(thresh)

# 5. Deskew (optional but helpful for tilted scans)
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, M, (w, h),
                          flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

deskewed = deskew(inverted)

# Optional: Resize to enlarge small text
scaled = cv2.resize(deskewed, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# 6. Save or use with OCR
cv2.imwrite("preprocessed.png", scaled)
