from src.mlflow import logger
from src.mlflow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlflow.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlflow.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.mlflow.pipeline.stage_04_model_traner import ModelTrainerTrainingPipeline
from src.mlflow.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

import mlflow
import dagshub

# Set the tracking URI for MLflow to point to DagsHub
mlflow.set_tracking_uri("https://dagshub.com/bijaycd/Wine-Quality-Prediction-using-MLfLow.mlflow")
dagshub.init(repo_owner='bijaycd', repo_name='Wine-Quality-Prediction-using-MLfLow', mlflow=True)

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e