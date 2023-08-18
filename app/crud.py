from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#비밀번호 해쉬값
def get_passwd_hash(password):
    return pwd_context.hash(password)

#비밀번호 증명
def verify_passwd(plan_passwd, hashed_passwd):
    return pwd_context.verify(plan_passwd, hashed_passwd)

# print(get_passwd_hash('1234'))  테스트
# end_pwd = get_passwd_hash('1234')
# print(end_pwd)
# print(verify_passwd('hello', end_pwd))