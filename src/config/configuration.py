from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity import DataIngestionConfig,PrepareBaseModelConfig,CallbackConfig
import os


class ConfigurationManager():
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.data_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            download_url=config.download_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    

    def get_prepare_base_model_config(self)->PrepareBaseModelConfig:
            config = self.config.prepare_base_model
            model_config = PrepareBaseModelConfig(
                root_dir = config.root_dir,
                base_model_path = config.base_model_path,
                updated_base_model_path = config.updated_base_model_path,
                params_image_size = self.params.IMAGE_SIZE[:-1],
                params_learning_rate = self.params.LEARNING_RATE,
                params_include_top = self.params.INCLUDE_TOP,
                params_weights = self.params.WEIGHTS,
                params_classes = self.params.CLASSES
            )
            return model_config
    
    def get_the_callback_config(self) -> CallbackConfig:
        config = self.config.save_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)

        create_directories([Path(model_ckpt_dir),Path(config.tensorboard_root_log_dir)])

        prepare_config_callback = CallbackConfig(
            root_dir = config.root_dir,
            tensorboard_root_log_dir = config.tensorboard_root_log_dir,
            checkpoint_model_filepath = config.checkpoint_model_filepath
        )
        return prepare_config_callback