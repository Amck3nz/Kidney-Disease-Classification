import os                       
from pathlib import Path
import logging 

"""
Executing this file will create the below folders
"""

# Logging String   
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')   # Current time stamp + log message

project_name = 'Temp'      # Template name, change as needed

# list of files/folder
list_of_files = [
    ".github/workflows/.gitkeep",                       # .gitkeep folder because wont be uploaded if empty
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",       # All components: data prep, model training, etc
    f"src/{project_name}/utils/__init__.py",            # Utility files
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "RnD/test.ipynb",
    "templates/index.html",                              # Because going to use flask endpoint
    "test.py"


]

for filepath in list_of_files:                                                  
    filepath = Path(filepath)                                                   # Giving entire path 1 by 1 to Path class bc forward slash may cause error for windows
    filedir, filename = os.path.split(filepath)                                 # Separate folder path and filename

    if filedir != "":                                                           
        os.makedirs(filedir, exist_ok=True)                                     # Make folder and log creation
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):      # If file doesnt exist or file size = 0, create file and log creation
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")