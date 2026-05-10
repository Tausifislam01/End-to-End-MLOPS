import pandas as pd
from sklearn.model_selection import train_test_split

from end_to_end_mlops.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self) -> None:
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data, test_size=0.25, random_state=42)
        train.to_csv(f"{self.config.root_dir}/train.csv", index=False)
        test.to_csv(f"{self.config.root_dir}/test.csv", index=False)

