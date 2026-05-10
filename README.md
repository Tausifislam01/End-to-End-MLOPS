# End-to-End MLOps Project with MLflow

An end-to-end machine learning project for wine quality prediction using FastAPI, MLflow, Docker, and GitHub Actions.

## Workflow

1. Update `config/config.yaml`
2. Update `schema.yaml`
3. Update `params.yaml`
4. Update entity classes
5. Update the configuration manager
6. Update components
7. Update pipelines
8. Run training
9. Run the FastAPI app

## Run Locally

```bash
pip install -r requirements.txt
python main.py
uvicorn app:app --host 0.0.0.0 --port 8080
```

## Docker

```bash
docker build -t wine-quality-fastapi .
docker run -p 8080:8080 wine-quality-fastapi
```

## MLflow

```bash
mlflow ui
```

Set tracking credentials through environment variables when using a remote MLflow server.

## Citation

This project follows the structure of Krish Naik's guided end-to-end MLflow project and adapts the application layer to FastAPI.
