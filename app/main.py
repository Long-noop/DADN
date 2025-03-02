from fastapi import FastAPI
from .database import get_db_connection
from .mqtt_handler import client  # Import để chạy MQTT
import json

app = FastAPI()

@app.get("/api/sensor")
def get_sensor_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sensor_data ORDER BY created_at DESC LIMIT 10")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"data": results}
