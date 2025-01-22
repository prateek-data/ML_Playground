FROM python:3.9-slim-bullseye

ENV MODEL_DIR='model_directory'

RUN mkdir -p ML_FLOW

COPY model_directory/ ML_FLOW/model_directory
COPY run_inference.py ML_FLOW
COPY requirements.txt ML_FLOW

EXPOSE 7000

WORKDIR ML_FLOW

RUN pip install -r requirements.txt

CMD ["python", "run_inference.py", "-m", "simple_model.pkl"]