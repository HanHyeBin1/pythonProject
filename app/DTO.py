from pydantic import BaseModel
from datetime import date, datetime, time, timedelta
from typing import Union

#schemas 대신 DTO 파일 작성

#token
class Token(BaseModel):
    access_token:str

#users 테이블
class Users(BaseModel):
    name: str
    password: str
    email: str
    email_check: bool
    address: str
    profil_image: str
    ninkName: str
    login_date: date
    phoneNum: str

#order테이블
class Order(BaseModel):
    order_date: date
    request_info: str
    order_status: str
    items_count: int
    price: int

#cart
class Carts(BaseModel):
    itmes_count: int

#category
class Category(BaseModel):
    category_name:str

#items
class itmes(BaseModel):
    item_name: str
    price: int
    item_info: str
    remain_item: int
    author_name: str
    author_info: str
    view_count: int
    register_date: date
    brand: str