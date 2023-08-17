from pydantic import BaseModel
from datetime import date, datetime, time, timedelta
from typing import Union

#users 테이블
class Users(BaseModel):
    name: str
    password: str
    email: str
    email_check: bool
    address: str
    profil_image: str
    ninkName: str
    login_date: str
    phoneNum: str