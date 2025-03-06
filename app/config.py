from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MQTT_BROKER: str
    MQTT_PORT: int
    AIO_USERNAME: str
    AIO_KEY: str
    AIO_FEED_ID: str

    class Config:
        env_file = ".env"

settings = Settings()
