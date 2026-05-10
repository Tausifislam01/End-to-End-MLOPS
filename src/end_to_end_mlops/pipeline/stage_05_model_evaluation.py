from end_to_end_mlops.components.model_evaluation import ModelEvaluation
from end_to_end_mlops.config.configuration import ConfigurationManager


STAGE_NAME = "Model Evaluation stage"


class ModelEvaluationTrainingPipeline:
    def main(self) -> None:
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    obj = ModelEvaluationTrainingPipeline()
    obj.main()

