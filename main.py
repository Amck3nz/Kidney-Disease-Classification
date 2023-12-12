from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


# Data Ingestion  ------------------------------------------------------------------
try:
    logger.info(f">>>>>> Data Ingestion: [started] <<<<<<")
    data_ingest = DataIngestionTrainingPipeline()
    data_ingest.main()
    logger.info(f">>>>>> Data Ingestion: [completed] <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# Base Model Preparation  ------------------------------------------------------------------
try:
    logger.info(f"********************")
    logger.info(f">>>>> Base Model Prep: [started] <<<<<")
    prep_base_model = PrepareBaseModelTrainingPipeline()
    prep_base_model.main()
    logger.info(f">>>>>> Base Model Prep: [completed] <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# Model Training  ------------------------------------------------------------------
try:
    logger.info(f"********************")
    logger.info(f">>>>> Model Training: [started] <<<<<")
    trainer = ModelTrainingPipeline()
    trainer.main()
    logger.info(f">>>>> Model Training: [completed] <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

    
# Model Evaluation  ------------------------------------------------------------------
try:
    logger.info(f"********************")
    logger.info(f">>>>> Model Evaluation: [started] <<<<<")
    evaluator = EvaluationPipeline()
    evaluator.main()
    logger.info(f">>>>> Model Evaluation: [completed] <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
