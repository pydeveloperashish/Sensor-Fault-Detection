from sensor.exception import SensorExecption
from sensor.logger import logging
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
import os
import sys
import pandas as pd
import numpy as np
from typing import Optional
import json


class SensorData:
    """
    This class help to export entire mongo db record as pandas DataFrame
    """
    
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name = DATABASE_NAME)
        except Exception as e:
            raise SensorExecption(e, sys)
        
    def export_collection_as_dataframe(
        self, collection_name : str, 
        database_name : Optional[str] = None) -> pd.DataFrame:
        try:
            """
            export entire collection as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            
            if "_id" in df.columns.to_list():
                df = df.drop(columns = ["_id"], axis = 1)
            df.replace({"na" : np.nan}, inplace = True)
            
            return df
        
        except Exception as e:
            raise SensorExecption(e, sys)
        
    