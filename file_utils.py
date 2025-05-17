import os
import sys
import pathlib



def set_args(input_path):
    if len(sys.argv) == 2:
        global file_path
        file_path = pathlib.Path(f"{input_path}\{sys.argv[1]}")
        print(f"File Path: {file_path}")
        return file_path
        
    elif len(sys.argv) == 1:
        raise TypeError("Error: Expected exactly one argument (path to file), but received none.\nUsage: python script.py <path_to_file>")

    else:
        raise TypeError("Error: Expected exactly one argument (path to file), but received multiple.\nUsage: python script.py <path_to_file>")

def file_exists(file_path: pathlib.Path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    
    return

def get_file_type(file_path):
    img_ext = [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif"]
    file_ext = file_path.suffix
    
    if file_ext == ".pdf":
        return "pdf"
    
    elif file_ext in img_ext:
        return "image"
    
    else:
        raise TypeError(f"Error: File type {file_ext} not supported.")