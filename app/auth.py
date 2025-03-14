from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
import firebase_admin
from firebase_admin import credentials, firestore

# 1️⃣ Cấu hình JWT
SECRET_KEY = "your-secret-key" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 2️⃣ Khởi tạo Firebase
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 3️⃣ Cấu hình mật khẩu
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 4️⃣ OAuth2 password bearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 5️⃣ Hàm mã hóa mật khẩu
def hash_password(password: str):
    return pwd_context.hash(password)

# 6️⃣ Kiểm tra mật khẩu
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 7️⃣ Tạo JWT token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 8️⃣ Xác thực token
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

# 9️⃣ API đăng nhập
def authenticate_user(username: str, password: str):
    user_ref = db.collection("users").where("username", "==", username).stream()
    users = [user.to_dict() for user in user_ref]
    if not users or not verify_password(password, users[0]["password"]):
        return False
    return users[0]

