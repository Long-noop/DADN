from fastapi import FastAPI
import json
from firebase_admin import db
from .firebase_config import mqtt_client 
from .signal import send_signal
app = FastAPI()

@app.get("/")
def get_data():
    try:
        ref = db.reference('sensorData')
        data = ref.get()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/signal")
def api_send_signal(feed_id: str, value: str, user: str):
    """
    API gửi tín hiệu đến Adafruit IO và lưu lịch sử vào Firestore.
    """
    response = send_signal(feed_id, value, user)
    if response["status"] == "error":
        raise HTTPException(status_code=500, detail=response["message"])
    return response