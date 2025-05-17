# LIBRARY IMPORTS
import numpy as np
from PIL import Image
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
from pathlib import Path


# SCRIPT IMPORTS
import file_utils

project_root = Path(__file__).parent
input_path: Path = project_root.joinpath(project_root, "Input") # Input Folder path
output_path: Path = project_root.joinpath(project_root, "Output") # Output Folder path
file_path: Path = file_utils.set_args(input_path) # Path to file to be processed


if __name__ == "__main__":
    file_utils.file_exists(file_path) # throws FileNotFoundError if file does not exist
    file_type = file_utils.get_file_type(file_path) # throws TypeError if file type is not supported
    