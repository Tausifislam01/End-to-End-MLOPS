import json
from pathlib import Path
from typing import Any

import joblib
import yaml
from box import ConfigBox


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    with open(path_to_yaml, encoding="utf-8") as yaml_file:
        content = yaml.safe_load(yaml_file)
    return ConfigBox(content)


def create_directories(path_to_directories: list, verbose: bool = True) -> None:
    for path in path_to_directories:
        Path(path).mkdir(parents=True, exist_ok=True)


def save_json(path: Path, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_json(path: Path) -> ConfigBox:
    with open(path, encoding="utf-8") as file:
        content = json.load(file)
    return ConfigBox(content)


def save_bin(data: Any, path: Path) -> None:
    joblib.dump(value=data, filename=path)


def load_bin(path: Path) -> Any:
    return joblib.load(path)
