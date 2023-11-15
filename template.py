import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "wafer_fault_detection"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    # creating the directories
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"""Created directory {filedir} for file {filename}.""")
    
    # creating the files if not exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as fileref:
            pass  # creating an empty file
            logging.info(f"""File {filename} created successfully.""")
    else:
        logging.info(f"""File {filename} already exists.""")