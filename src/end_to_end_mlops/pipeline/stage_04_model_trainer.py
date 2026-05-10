from end_to_end_mlops.components.model_trainer import ModelTrainer
from end_to_end_mlops.config.configuration import ConfigurationManager


STAGE_NAME = "Model Trainer stage"


class ModelTrainerTrainingPipeline:
    def main(self) -> None:
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    obj = ModelTrainerTrainingPipeline()
    obj.main()

