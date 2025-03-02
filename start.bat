@echo off
echo running FastAPI server...

:: Kiểm tra và tạo venv nếu chưa có
if not exist venv (
    echo  create venv Python...
    python -m venv venv
)

:: Kích hoạt venv
call venv\Scripts\activate

:: Cài đặt thư viện cần thiết
@REM echo  Install Depentdencies...
@REM pip install -r requirements.txt

:: Chạy ứng dụng FastAPI
echo ✅ Server is running at http://localhost:8000
uvicorn app.main:app --host localhost --port 8000 --reload


