import sys
import firebase_admin
from firebase_admin import credentials, db
from .config import settings
import paho.mqtt.client as mqtt
import json 

cred = credentials.Certificate("dadn-e25c3-firebase-adminsdk-fbsvc-87fe5593ab.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://dadn-e25c3-default-rtdb.firebaseio.com/"
})

# Hàm callback khi nhận được message từ MQTT
def on_message(client, userdata, message):
    try:
        payload = message.payload.decode("utf-8")
        # data = json.loads(payload)
        
        # Ghi dữ liệu lên Firebase Realtime Database
        ref = db.reference('sensorData')
        ref.push().set({
            'value': payload,
            'timestamp': {".sv": "timestamp"}        
        })
        print(f"Data saved to Firebase: {payload}")
    except Exception as e:
        print(f"Error processing MQTT message: {e}")

# Kết nối MQTT
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(settings.AIO_USERNAME, settings.AIO_KEY)
mqtt_client.on_message = on_message

mqtt_client.connect(settings.MQTT_BROKER, settings.MQTT_PORT)
mqtt_client.subscribe(f"{settings.AIO_USERNAME}/feeds/{settings.AIO_FEED_ID}")
mqtt_client.loop_start()