from src.config.configuration import ConfigurationManager
from src.components.stage_03_model_chkpnt import PrepareCallback

class CallBackSavePipeline:
    def __init__(self):
        pass
        

    def main(self):
        config = ConfigurationManager()
        callback_config = config.get_the_callback_config()
        callback = PrepareCallback(config=callback_config)
        callback.get_tb_ckpt_callbacks()