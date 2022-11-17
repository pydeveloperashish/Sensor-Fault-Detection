from sensor.exception import SensorException
from sensor.logger import logging
import yaml
import numpy as np
import os,sys
import dill

def read_yaml_file(file_path : str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
            SensorException(e, sys)
            
    
def write_yaml_file(file_path : str, content : object, replace : bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok = True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
            SensorException(e, sys)
    

def save_numpy_array_data(file_path : str, array : np.array):
    """
    Save numpy array data from file
    file_path: str location of file to save
    return: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok = True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        SensorException(e, sys)
        
        
def load_numpy_array_data(file_path : str) -> np.array:
    """
    Load numpy array data from file
    file_path: str location of file to Load
    return: np.array data Loaded
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        SensorException(e, sys)
        
        
def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info("Entered the save_object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path), exist_ok = True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of MainUtils class")
    except Exception as e:
        raise SensorException(e, sys)