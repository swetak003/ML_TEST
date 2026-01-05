import os
import sys
from src.ML_Project.exceptions import CustomException
from src.ML_Project.logger import logging
import pandas as pd
from src.ML_Project.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:###watevr classes we are making we r putting in dataclass
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')#raw file & the data will be saved in artifacts folder

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()#object of the dataclass

    def initiate_data_ingestion(self):
        try:
            ## reading data from sql database
            df=read_sql_data()
            logging.info("Data Ingestion method starts")
        
            logging.info("Dataset read as pandas dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)#creating artifacts folder

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)#saving raw data

            logging.info("Raw data is saved")

        
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)#saving train data

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)#saving test data

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.error("Error in Data Ingestion")
            raise CustomException(e,sys)