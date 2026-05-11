import os


def set_env_variable(key: str, value: str) -> None:
    os.environ[key] = value


def get_env_variable(key: str, default: str = "") -> str:
    return os.getenv(key, default)

