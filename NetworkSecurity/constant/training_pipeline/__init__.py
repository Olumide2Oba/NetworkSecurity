import os
import sys
import pandas as pd      
import numpy as np 


'''
Definning common constant for training pipeline
'''                 
TARGET_COLUMN = "Result"
PIPELINE: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


'''
Data Ingestion related constant start with DATA_INGESTION
'''

DATA_INGESTION_COLLECTION_NAME = str = "NetworkData"
DATA_INGESTION_DATABASE_NAME = str = "Olumide"
DATA_INGESTION_DIR_NAME = str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = str = "feature_store"
DATA_INGESTION_INGESTED_DIR = str = "Ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = float = 0.2