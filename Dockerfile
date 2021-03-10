FROM python:3.8.6-buster

COPY scripts /scripts
COPY squatpro /squatpro
COPY weights.h5 /weights.h5
COPY my_model /my_model
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
RUN apt install libgl1-mesa-glx
RUN apt install ffmpeg -y

CMD streamlit run scripts/app.py

