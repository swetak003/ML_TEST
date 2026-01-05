import os
import sys
from src.ML_Project.exceptions import CustomException
from src.ML_Project.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()  # Load environment variables from a .env file if present

host=os.getenv('host')
user=os.getenv('user')   
password=os.getenv('password')
database=os.getenv('db')

def read_sql_data():
    logging.info("Reading data from SQL database")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        logging.info("Connection to database established successfully",mydb)

        query = "SELECT * FROM financial_loan"  # Replace with your actual table name
        df = pd.read_sql(query, mydb)
        logging.info("Data read successfully from SQL database")
        return df
    
    except Exception as e:
        logging.error("Error reading data from SQL database")
        raise CustomException(e, sys)
