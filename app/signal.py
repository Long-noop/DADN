from datetime import datetime
from .firebase_config import mqtt_client, dbfirestore
from .config import settings

def send_signal(feed_id: str, value: str, user: str):
    """
    Gửi tín hiệu đến Adafruit IO và lưu lịch sử vào Firestore.
    """
    try:
        # Gửi tín hiệu đến Adafruit IO
        topic = f"{settings.AIO_USERNAME}/feeds/{feed_id}"
        mqtt_client.publish(topic, value)
        print(f"✅ Gửi thành công: {feed_id} -> {value}")

        # Lưu lịch sử vào Firestore
        history_ref = dbfirestore.collection("control_history")
        history_ref.add({
            "feed_id": feed_id,
            "value": value,
            "user": user,
            "timestamp": datetime.utcnow()
        })
        print("✅ Lịch sử đã được lưu vào Firestore!")

        return {"status": "success", "message": "Tín hiệu đã được gửi và lưu lịch sử"}
    
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return {"status": "error", "message": str(e)}
