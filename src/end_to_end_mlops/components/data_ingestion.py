import urllib.request
import zipfile
from pathlib import Path

from end_to_end_mlops.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> None:
        local_file = Path(self.config.local_data_file)
        if not local_file.exists():
            urllib.request.urlretrieve(self.config.source_URL, local_file)

    def extract_zip_file(self) -> None:
        unzip_path = Path(self.config.unzip_dir)
        unzip_path.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)

