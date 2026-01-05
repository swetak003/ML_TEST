from src.ML_Project.logger import logging
from src.ML_Project.exceptions import CustomException
import sys
from src.ML_Project.components import data_ingestion
from src.ML_Project.components.data_ingestion import DataIngestion, DataIngestionConfig
#from src.ML_Project.components.data_transformation import DataTransformation, DataTransformationConfig
#from src.ML_Project.components.data_transformation import DataIngestionConfig
#from src.ML_Project.components.model_trainer import ModelTrainerConfig, ModelTrainer

if __name__ == "__main__":
    logging.info("Application started")
    # Your application code here
    logging.info("Application finished")

    try:
        # Simulate some operation that may raise an exception
        Data_ingestion=DataIngestion()
        Data_ingestion.initiate_data_ingestion()



    except Exception as e:
        logging.info("An error occurred")
        logging.error(f"Error details: {e}")
        raise CustomException(e, sys)