
import pandas as pd
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pipeline
import request


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def index():
    return {"ok": "True"}



@app.get("/predict/")

    response = request.file[#name in streamlite file].read()

   # build X ⚠️ beware to the order of the parameters ⚠️

    score = pipeline.predict_test(response)



    return {'score':score}
