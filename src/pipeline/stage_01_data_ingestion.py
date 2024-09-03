from src.components.stage_01_data_ingestion import DataIngestion
from src.config.configuration import ConfigurationManager

class Data_ingestion_pipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager().get_data_ingestion_config()
        data_ingestion = DataIngestion(config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()