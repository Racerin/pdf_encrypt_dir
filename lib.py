import os
import json
import logging

import PyPDF2
from PyPDF2 import PdfReader, PdfWriter

# Instantiating config dict
config_json_file_name = "config.json"
config = dict()
if os.path.exists(config_json_file_name):
    with open(config_json_file_name, mode="r") as file:
        config = json.load(file)

# DEFAULTS
DEF_DIR_PATH_pre = os.getcwd()
# DEF_DIR_PATH : str = config.get('read_dir_path',DEF_DIR_PATH_pre)
DEF_DIR_PATH : str = os.getcwd()
# if DEF_DIR_PATH is None: DEF_DIR_PATH = _DEF_DIR_PATH
assert isinstance(DEF_DIR_PATH, str), DEF_DIR_PATH

DEF_OUT_DIR_PATH_pre = os.path.join(DEF_DIR_PATH, r"out\encrypted")
DEF_OUT_DIR_PATH : str = config.get(
    'write_dir_path', 
    DEF_OUT_DIR_PATH_pre
    )
DEF_OUT_DIR_PATH = os.path.join(os.getcwd(), r'out')
# if DEF_OUT_DIR_PATH is None: DEF_DIR_PATH = DEF_OUT_DIR_PATH_pre
assert isinstance(DEF_OUT_DIR_PATH, str), DEF_OUT_DIR_PATH

DEF_PW = ""

def get_parent_directory(path:str):
    dirs = path.split("\\")
    parent_dir = "\\".join(dirs[:-1])
    return parent_dir
    
def is_directory_empty(dir_path:str):
    files = os.listdir(dir_path)
    for _ in files: return False
    return True

def pdf_file_in_list(list1:list[str])->bool:
    """ Boolean expressing whether list contains a pdf file name """
    return any( (file.endswith('.pdf') for file in list1) )

def filter_pdf_files(paths:list[str])->list[str]:
    """ Return a list of files ending with '.pdf' """
    assert all(isinstance(ele,str) for ele in paths), "Each element should be a str"
    pdf_files = list()
    for path in paths:
        if path.endswith('pdf'):
            pdf_files.append(path)
    return pdf_files

def clean_up_empty_directory(directory)->None:
    """ 
    Remove directory if it's empty.
    *Subject to change:
    - Function was created to clean-up any directory created by 
    'encrypt_PDFs_in_directory' if a PDF file was failed to be created.
    """

def encrypt_pdf(
        read_pdf_path:str,
        write_pdf_path:str,
        owner_password:str,
        user_password:str=None,
        )->None:
    """ Writes an encrypted PDF file to 'out directory'. """
    # Fix defaults
    if user_password is None:
        user_password=owner_password
    # Read previous PDF to format encrypted PDF
    reader = PdfReader(read_pdf_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    # Encrypt new PDF
        # Reference: https://pypdf2.readthedocs.io/en/3.0.0/modules/PdfWriter.html#PyPDF2.PdfWriter.encrypt
    writer.encrypt(
        user_password=user_password,
        owner_password=owner_password,
        use_128bit=True,
        permissions_flag=0b0000000000,
        )
    # Write encrypted PDF file
    with open(write_pdf_path, "wb") as f:
        writer.write(f)

def encrypt_PDFs_in_directory(
        owner_password:str,
        user_password:str,
        dir_path:str,
        write_dir_path:str,
        ):
    first_root_directory = None
    for root,_dirs,files in os.walk(dir_path):
        # Catch the 1st root directory
        if first_root_directory is None: first_root_directory = root
        # Go through each directory containing PDF files
        pdf_files = filter_pdf_files(files)
        if pdf_files:
            relative_dir_path = os.path.relpath(root, first_root_directory)
            for pdf_file_name in pdf_files:
                write_pdf_path = os.path.join(write_dir_path,relative_dir_path, pdf_file_name)
                read_pdf_path = os.path.join(root, pdf_file_name)
                # Ensure Directory exists
                write_dir = get_parent_directory(write_pdf_path)
                os.makedirs(write_dir, exist_ok=True)
                try:
                    encrypt_pdf(read_pdf_path, write_pdf_path, owner_password, user_password)
                except PyPDF2.errors.FileNotDecryptedError:
                    logging.warning(f"File '{write_pdf_path}' is encrypted already.")
                else:
                    continue
                # This code runs if any Exception occures once 'return' exists under 'else'
                # Reference: https://stackoverflow.com/a/12279318
                # MIGHT NOT BE COMPLETE (child of child directory)
                if is_directory_empty(write_dir):
                    os.rmdir(write_dir)
                