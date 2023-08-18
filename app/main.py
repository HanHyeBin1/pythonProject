from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
from pydantic import BaseModel
from passlib.context import CryptContext
from DTO import Users
from logger import mylogger
from database import get_db, SessionLocal
import jwt

app = FastAPI()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

db = SessionLocal()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#비밀번호 해쉬값
def get_passwd_hash(password):
    return pwd_context.hash(password)

#비밀번호 증명
def verify_passwd(plan_passwd, hashed_passwd):
    return pwd_context.verify(plan_passwd, hashed_passwd)

#테스트
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

#로그인
@app.post("/login")
def login(user: Users):
    mylogger.debug(user)
    #사용자의 비밀번호 해시화 하기
    user.password = get_passwd_hash(user.password)
    #유저를 DB에 저장 / db 연결해야함
    db.session.add(user)
    db.session.commit()
    return {"message": "User login successfully"}

#회원가입
@app.post("/signup")
def signup(user: Users):
    mylogger.debug(user)
    return {"message": "User registered successfully"}

#이메일 확인
@app.get("/email-check")
def emaincheck():
    mylogger.debug("email check function")
    return {"message": "Email is available"}

#로그아웃
@app.post("/logout")
def logout():
    mylogger.debug("logout")
    return {"message": "User logout successfully"}

#회원정보 삭제
@app.delete("/users")
def userdelete():
    mylogger.debug("user delete")
    return {"message": "User delete successfully"}

#장바구니 추가
@app.post("/carts/{user_no}")
def addcarts():
    mylogger.debug("carts 추가")
    return {"message": "아이템이 장바구니에 추가되었습니다."}

#장바구니 조회
@app.get("/carts/{user_no}")
def usercarts():
    mylogger.debug("장바구니조회")
    return {"message":"장바구니 조회"}

#고객 주문 상세페이지
@app.get("/order/{order_no}")
def order():
    mylogger.debug("주문 상세 페이지")
    return {"message":"주문 상세 페이지"}

@app.delete("/order/{order_no}")
def orderdelete():
    mylogger.debug("order delete")
    return {"message": "order delete successfully"}

@app.patch("/orders/{order_no}/{order_status}")
def orderStatus():
    mylogger.debug("주문 상태 변경")
    return {"message": "주문 상태 변경 완료"}

@app.post("/items")
def inserItems():
    mylogger.debug("아이템 추가")
    return { "message": "items insert successfully"}

@app.get("/items")
def showItems():
    mylogger.debug("아이템 조회")
    return { "message": "items show successfully"}

@app.get("/items/{item_no}")
def showItems():
    mylogger.debug("아이템 상세 조회")
    return { "message": "items show successfully"}

@app.delete("/items/{item_no}")
def deleteItems():
    mylogger.debug("아이템 삭제")
    return { "message": "items delete successfully"}

@app.patch("/items/{item_no}")
def remainItems():
    mylogger.debug("아이템 재고")
    return { "message": "items remain successfully"}