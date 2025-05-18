# LIBRARY IMPORTS
import sys
from pathlib import Path
from pdf2image import convert_from_path

# FUNCTIONS
def set_args(input_path):
    file_path: list[Path] = []

    if len(sys.argv) > 1:
        args = list(sys.argv[1:])
        print(args)
        for i, arg in enumerate(args):
            file_path.append(input_path.joinpath(arg))
            #print(f"File{i+1} Path: {arg}")

        return file_path

    else:
        raise TypeError("Error: Expected at least one argument (name of file), but none were given.\nUsage: python script.py <name_of_file>")

def file_exists(file_path: list[Path]):
    exception_str: str = ""
    for path in file_path:
        if not path.is_file():
            exception_str += f"\nFile {path.name} not found."
        else:
            print(f"File {path} found.")
    
    if exception_str:
        raise FileNotFoundError(f"{exception_str}")
    
    return

def check_file_type(file_paths):
    img_ext = [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif"]
    pdf_paths: list[Path] = []

    for path in file_paths:
        file_ext = path.suffix

        if file_ext == ".pdf":
            pdf_paths.append(path)
    
        elif file_ext in img_ext:
            continue
    
        else:
            raise TypeError(f"Error: File type {file_ext} not supported.")
    
    if pdf_paths:
        pdf_to_image(pdf_paths)
    
def pdf_to_image(pdf_paths: list[Path]):
    img_paths: list[Path] = []
    images = []
    for pdf_file in pdf_paths:
        images = convert_from_path(pdf_file, dpi=300)

        for i, img in enumerate(images):
            path = Path(f"{pdf_paths[:-4]}_{i}.png")
            img.save(path, "PNG")
            img_paths.append(path)

    return img_paths

def get_image_paths(input_path):
    pass