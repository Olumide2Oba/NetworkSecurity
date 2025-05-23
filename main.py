from NetworkSecurity.components.data_ingestion import DataIngestion
from NetworkSecurity.entity.config_entity import DataIngestionConfig
from NetworkSecurity.logging import logger
from NetworkSecurity.entity.artifact_entity import DataIngestionArtifact
from NetworkSecurity.entity.config_entity import TrainingPipelineConfig
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
import sys 

if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)