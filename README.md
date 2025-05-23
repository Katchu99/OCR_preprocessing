# Disclaimer (Work in Progress)

This project is in the very early stages of development. Core functionality, including PDF and image preprocessing for OCR enhancement, is not fully implemented yet.

Use this repository for experimental purposes only. Features, interfaces, and behaviors are subject to significant changes.

Contributions, feedback, and collaboration are highly encouraged to help shape the project.

# OCR Preprocessing

**OCR Preprocessing** is a Python utility for preparing PDF and image files to maximize **OCR (Optical Character Recognition)** accuracy.  
It focuses purely on **preprocessing**, such as image cleanup and conversion — the actual OCR is performed by external tools.  
This script is optimized for use in **RPA workflows**, especially with **UiPath**.

---

## Features

- **PDF to Image Conversion**: Converts PDF files to high-resolution images for better downstream OCR performance.
- **Image Enhancement**: Applies techniques like grayscale conversion, binarization, and noise reduction.
- **Batch Processing**: Handles multiple files and outputs cleaned image files to a designated directory.
- **Image Path Export**: Saves processed image paths for easy handoff to OCR systems.

---

## Prerequisites

- Python 3.7+
- [Poppler](https://poppler.freedesktop.org/) (for PDF to image conversion)
- Python dependencies listed in `requirements.txt` (e.g., `pdf2image`, `opencv-python`)

## Installation

```bash
git clone https://github.com/Katchu99/OCR_preprocessing.git
cd OCR_preprocessing

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run the script by passing the input directory or filenames (PDF or image):

```bash
python main.py <name_of_file_or_directory>

```

---

## Integration with UiPath

This script is ideal for preprocessing files before OCR in UiPath:

1. **Invoke Python Script** in UiPath to call the preprocessing step.
2. **Pass File Paths** as arguments to the script.
3. **Get Processed Image Paths** from the script’s output.
4. **Perform OCR** on those enhanced images using UiPath's OCR engine.

> 🔍 **Note:** This script does **not** perform OCR directly — it prepares images to improve OCR reliability and accuracy.

---

## Contributing

Contributions, suggestions, and issues are welcome. Please fork and submit a pull request.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
