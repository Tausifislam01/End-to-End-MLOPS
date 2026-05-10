from end_to_end_mlops.components.data_transformation import DataTransformation
from end_to_end_mlops.config.configuration import ConfigurationManager


STAGE_NAME = "Data Transformation stage"


class DataTransformationTrainingPipeline:
    def main(self) -> None:
        with open("artifacts/data_validation/status.txt", encoding="utf-8") as file:
            status = file.read().split(" ")[-1]

        if status != "True":
            raise Exception("Data schema is not valid")

        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()


if __name__ == "__main__":
    obj = DataTransformationTrainingPipeline()
    obj.main()

