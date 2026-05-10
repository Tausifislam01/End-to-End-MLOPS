from end_to_end_mlops.components.data_ingestion import DataIngestion
from end_to_end_mlops.config.configuration import ConfigurationManager


STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def main(self) -> None:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    obj = DataIngestionTrainingPipeline()
    obj.main()

