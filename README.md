# **IoT API Server with FastAPI**

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)  
![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)

This project is an **IoT API server** built using **FastAPI** in Python. It receives sensor data via **MQTT**, stores it in **Firebase Realtime Database**, and provides RESTful APIs to retrieve the data. The project also uses **venv** for virtual environment management and **.env** for environment variables.

---

## **Features**

- **Real-time data ingestion**: Receive sensor data via MQTT.
- **Data storage**: Store sensor data in Firebase Realtime Database.
- **RESTful API**: Retrieve sensor data via FastAPI endpoints.
- **Environment management**: Use `.env` for security configuration and `venv` for dependency isolation.

---

## **Technologies Used**

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Firebase Realtime Database**: A cloud-hosted NoSQL database for real-time data storage.
- **MQTT**: A lightweight messaging protocol for IoT devices.
- **Python**: The primary programming language.

---

## **Project Structure**
```py
DADN/
├── app/
│   ├── main.py               # FastAPI server and endpoints
│   ├── firebase_config.py    # Firebase and MQTT configuration
│   ├── config.py             # Application configuration
│   ├── models.py             # Data models (Pydantic)
├── .env                      # Environment variables
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation

```

---

## **Installation**

### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/iot-api.git
cd iot-api
```

### **2. Set Up Virtual Environment**

Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Linux/MacOS
venv\Scripts\activate     # On Windows
```

### **3. Install Dependencies**

Install the required packages:
```sh
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**

Create a .env file in the root directory and add the following variables:
```sh
MQTT_BROKER=io.adafruit.com
MQTT_PORT=1883
AIO_USERNAME=your_adafruit_username
AIO_KEY=your_adafruit_key
AIO_FEED_ID=your_feed_id
```
5. Run the Server

Start the FastAPI server:
```sh
uvicorn main:app --reload
```
The server will be available at http://localhost:8000.
