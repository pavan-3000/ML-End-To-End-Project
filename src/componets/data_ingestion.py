import os
from src.logger import logging
from src.exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifact','train.csv')
    test_data_path:str = os.path.join('artifact','test.csv')
    raw_data_path:str = os.path.join('artifact','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_confi=DataIngestionConfig()

    def inciate_data_ingestion(self):
        logging.info("data injestion")
        try:
            df = pd.read_csv("train.csv")
            logging.info("data reading")

            os.makedirs(os.path.dirname(self.ingestion_confi.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_confi.raw_data_path,index=False,header=True)
            logging.info("split data")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=43)
            train_set.to_csv(self)
        except:
            pass