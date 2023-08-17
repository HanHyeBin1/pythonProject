from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel
from DTO import Users
from logger import mylogger

app = FastAPI()


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

#로그인
@app.post("/login")
def login(user: Users):
    mylogger.debug(user)
    return {"message": "User login successfully"}

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