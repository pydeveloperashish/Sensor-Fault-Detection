from sensor.config.mongo_db_connection import MongoDBClient
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.exception import SensorException
from sensor.logger import logging
import os
import sys



if __name__ == '__main__':
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()
