import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME

"""
Defining Constant for training pipeline
"""

TARGET_COLUMN = "class"
PIPELINE_NAME : str = "sensor"
ARTIFACT_DIR : str = "artifacts"
FILE_NAME : str = "sensor.csv"

TRAIN_FILE_NAME : str = "train.csv"
TEST_FILE_NAME  : str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME  = "model.pkl"
SCHEMA_FILE_NAME =  os.path.join("config", "schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME 
"""

DATA_INGESTION_COLLECTION_NAME : str = "myFirstCollection"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature-store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION : float = 0.2



