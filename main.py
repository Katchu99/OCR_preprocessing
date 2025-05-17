# LIBRARY IMPORTS
import numpy as np
from PIL import Image
from pdf2image import convert_from_path
from pathlib import Path


# SCRIPT IMPORTS
import file_utils
import image_utils

project_root = Path(__file__).parent
input_path: Path = project_root.joinpath(project_root, "Input") # Input Folder path
output_path: Path = project_root.joinpath(project_root, "Output") # Output Folder path
file_paths: list[Path] = file_utils.set_args(input_path) # Path to file to be processed


if __name__ == "__main__":
    file_utils.file_exists(file_paths) # throws FileNotFoundError if file does not exist
    file_utils.check_file_type(file_paths) # throws TypeError if file type is not supported and converts pdfs to images
    image_paths = file_utils.get_image_paths()

