import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name=   "ML_Project"
project_version= "0.1.0"
list_of_files=[".github/workflows/.gitkeep",
               f"src/{project_name}/__init__.py",
               f"src/{project_name}/components/__init__.py",
               f"src/{project_name}/components/data_ingestion.py",
               f"src/{project_name}/components/data_transformation.py",
               f"src/{project_name}/components/model_trainer.py",
               f"src/{project_name}/components/model_monitering.py",
               f"src/{project_name}/pipelines/__init__.py",
               f"src/{project_name}/pipelines/training_pipeline.py",
               f"src/{project_name}/pipelines/prediction_pipeline.py",
               f"src/{project_name}/exceptions/__init__.py",
               f"src/{project_name}/config/__init__.py",
               f"src/{project_name}/config/configuration.py",
                f"src/{project_name}/config/mapper.py",
                f"src/{project_name}/logger/__init__.py",
               f"src/{project_name}/utils/__init__.py",
               "requirements.txt",
               "setup.py",
               "research/trials.ipynb",
               "app.py"
]
for filepath in list_of_files:
    filepath=Path(filepath)
    file_dir,filename=os.path.split(filepath)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {filepath}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath,'w') as f:
            pass
        logging.info(f"Created empty file: {filepath}")

    else:
        logging.info(f"File already exists and is not empty: {filepath}")
