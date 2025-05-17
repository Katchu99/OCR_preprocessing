from pdf2image import convert_from_path
from PIL import Image
from pathlib import Path

def pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path, dpi=300)
    img_paths: list[Path] = []
    
    for i, img in enumerate(images):
        path = Path(f"{pdf_path[:-4]}_{i}.png")
        img.save(path, "PNG")
        img_paths.append(path)

    return img_paths