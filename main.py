from src.winequality.logging import logger
from winequality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"=======stage {STAGE_NAME} started ========")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"=======stage {STAGE_NAME} completed ========\n\nx========n")

except Exception as e:
    logger.exception(e)    
    raise e