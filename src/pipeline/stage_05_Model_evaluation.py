from src.components.stage_05_model_eval import ModelEvaluation
from src.config.configuration import ConfigurationManager
from pathlib import Path


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager().get_model_eval_config()
        eval_config = ModelEvaluation(config=config)
        eval_config.evaluation()
        eval_config.save_score()