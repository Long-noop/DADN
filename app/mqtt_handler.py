import paho.mqtt.client as mqtt
from .database import get_db_connection
from .config import settings

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    print(f"📩 Nhận dữ liệu từ {msg.topic}: {data}")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO sensor_data (temperature, created_at) VALUES (%s, NOW())"
        cursor.execute(sql, (data,))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Dữ liệu đã được lưu vào database!")
    except Exception as e:
        print(f"❌ Lỗi khi lưu dữ liệu: {e}")

# Kết nối MQTT
client = mqtt.Client()
client.username_pw_set(settings.AIO_USERNAME, settings.AIO_KEY)
client.on_message = on_message
client.connect(settings.MQTT_BROKER, settings.MQTT_PORT)
client.subscribe(f"{settings.AIO_USERNAME}/feeds/{settings.AIO_FEED_ID}")
client.loop_start()
