import os, sys
import pandas as pd 
import numpy as np 

from src.exception import CustomException
from src.logger import logging

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_path:str = os.path.join('artifacts', 'train_data.csv')
    test_path:str = os.path.join('artifacts', 'test_data.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestionconfig = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Data ingestion process started")

            df = pd.read_csv("wine.csv")

            os.makedirs(os.path.dirname(self.ingestionconfig.train_path), exist_ok=True)

            df.to_csv(self.ingestionconfig.raw_data_path, index=False, header=True)
            print(df.shape)
            logging.info("Data imported")

            df = df.drop_duplicates()
            print(df.shape)

            from sklearn.model_selection import train_test_split
            train_data, test_data = train_test_split(df, test_size=0.3, random_state=42)

            logging.info("Train test split initiated")

            train_data.to_csv(self.ingestionconfig.train_path, index = False, header = True)
            test_data.to_csv(self.ingestionconfig.test_path, index = False, header = True)

            logging.info("Train test split completed and ingestion process sucessfull")

            return(
                self.ingestionconfig.train_path,
                self.ingestionconfig.test_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        

if __name__=="__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()