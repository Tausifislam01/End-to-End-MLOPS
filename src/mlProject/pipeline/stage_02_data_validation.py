from mlProject.components.data_validation import DataValidation
from mlProject.config.configuration import ConfigurationManager


STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
    def main(self) -> None:
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == "__main__":
    obj = DataValidationTrainingPipeline()
    obj.main()

