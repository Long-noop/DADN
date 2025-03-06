# import paho.mqtt.client as mqtt
# from .firebase_config import get_db_reference
# from .config import settings

# def on_message(client, userdata, msg):
#     data = msg.payload.decode()
#     print(f"📩 Nhận dữ liệu từ {msg.topic}: {data}")

#     try:
#         # Lấy tham chiếu Firebase
#         ref = get_db_reference()
#         sensor_data = {
#             "temperature": float(data),
#             "timestamp": datetime.datetime.utcnow().isoformat()
#         }

#         # Lưu vào Firebase
#         ref.child("sensor_data").push(sensor_data)
#         print("✅ Dữ liệu đã được lưu vào Firebase!")
#     except Exception as e:
#         print(f"❌ Lỗi khi lưu dữ liệu: {e}")

# # Kết nối MQTT
# client = mqtt.Client()
# client.username_pw_set(settings.AIO_USERNAME, settings.AIO_KEY)
# client.on_message = on_message
# client.connect(settings.MQTT_BROKER, settings.MQTT_PORT)
# client.subscribe(f"{settings.AIO_USERNAME}/feeds/{settings.AIO_FEED_ID}")
# client.loop_start()
