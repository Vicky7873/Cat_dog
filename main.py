from src.pipeline.stage_01_data_ingestion import Data_ingestion_pipeline
from src import logger
from src.pipeline.stage_02_Base_model import PrepareBaseModelPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Data_ingestion_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.run_pipeline()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e



