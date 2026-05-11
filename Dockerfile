FROM python:3.10-slim-bookworm

WORKDIR /app

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONPATH=/app/src

COPY requirements.txt /app/
RUN grep -v '^-e[[:space:]]*\.$' requirements.txt > requirements-docker.txt \
    && pip install -r requirements-docker.txt
RUN pip install --no-cache-dir "setuptools<70"

ENV GIT_PYTHON_REFRESH=quiet

COPY . /app
RUN python main.py

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
