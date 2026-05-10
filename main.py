from end_to_end_mlops.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from end_to_end_mlops.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from end_to_end_mlops.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from end_to_end_mlops.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from end_to_end_mlops.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGES = [
    DataIngestionTrainingPipeline,
    DataValidationTrainingPipeline,
    DataTransformationTrainingPipeline,
    ModelTrainerTrainingPipeline,
    ModelEvaluationTrainingPipeline,
]


if __name__ == "__main__":
    for stage in STAGES:
        stage().main()

