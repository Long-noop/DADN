from fastapi import FastAPI
import paho.mqtt.client as mqtt
import mysql.connector
import json

# Khởi tạo FastAPI
app = FastAPI()

# Cấu hình MQTT
MQTT_BROKER = ""
MQTT_TOPIC = ""

# Cấu hình MySQL
db = mysql.connector.connect(
    host="",
    user="",
    password="",  
    database=""
)
cursor = db.cursor()

# Hàm xử lý khi nhận dữ liệu MQTT
def on_message(client, userdata, msg):
    data = msg.payload.decode()
    print(f"📩 Nhận dữ liệu từ {msg.topic}: {data}")
    
    # Lưu vào database
    sql = "INSERT INTO sensor_data (temperature, created_at) VALUES (%s, NOW())"
    cursor.execute(sql, (data,))
    db.commit()
    print("✅ Dữ liệu đã được lưu vào database!")

# Kết nối MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, 1883)
client.subscribe(MQTT_TOPIC)
client.loop_start()

# API lấy dữ liệu từ database
@app.get("/api/sensor")
def get_sensor_data():
    cursor.execute("SELECT * FROM sensor_data ORDER BY created_at DESC LIMIT 10")
    results = cursor.fetchall()
    return {"data": results}

# Chạy server FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
