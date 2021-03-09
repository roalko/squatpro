FROM python:3.8.6-buster

COPY scripts /scripts
COPY squatpro /squatpro
COPY weights.h5 /weights.h5
COPY my_model /my_model
COPY requirements.txt /requirements.txt
COPY pipeline.py /pipeline.py

RUN pip install -r requirements.txt

CMD uvicorn fast:app --host 0.0.0.0 --port $PORT
