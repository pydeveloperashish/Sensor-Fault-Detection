import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME

SAVED_MODEL_DIR = os.path.join("saved_models")

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
Data Ingestion related constant starts with DATA_INGESTION VAR NAME 
"""

DATA_INGESTION_COLLECTION_NAME : str = "myFirstCollection"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature-store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION : float = 0.2


"""
Data Validation related content starts with DATA_VALIDATION VAR NAME.
"""

DATA_VALIDATION_DIR_NAME : str = "data_validation"
DATA_VALIDATION_VALID_DIR : str = "validated"
DATA_VALIDATION_INVALID_DIR : str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = "report.yaml"


"""
Data Transformation related constants starts with DATA_TRANSFORMATION VAR NAME.
"""
DATA_TRANSFORMATION_DIR_NAME : str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DIR_NAME : str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR : str = "transformed_object"



"""
Model Trainer related constants starts with MODEL_TRAINER VAR NAME.
"""

MODEL_TRAINER_DIR_NAME : str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR : str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME : str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE : float = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD : float = 0.05   # 5% difference



"""
Model Evaluation related constants starts with MODEL_EVALUATION VAR NAME
"""

MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE : float = 0.02   # 2% 
MODEL_EVALUATION_DIR_NAME : str = "model_evaluation"
MODEL_EVALUATION_REPORT_NAME : str = "report.yaml"


