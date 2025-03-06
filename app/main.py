from fastapi import FastAPI
import json
from firebase_admin import db
from .firebase_config import mqtt_client 

app = FastAPI()

@app.get("/")
def get_data():
    try:
        ref = db.reference('sensorData')
        data = ref.get()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/sensor")
def get_sensor_data():
    try:
        ref = db.reference('sensorData')
        data = ref.get()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
