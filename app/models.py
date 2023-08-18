from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import date, datetime, time, timedelta

from .database import Base


class User(Base):
    __tablename__ = "users"

    user_no = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email_check = Column(bool)
    address = Column(String)
    profil_image = Column(String)
    ninkName = Column(String)
    login_date = Column(datetime)
    phoneNum = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    item_info = Column(String, index=True)
    price = Column(int)
    remain_item = Column(int)
    author_name = Column(String)
    view_count = Column(int)
    register_date = Column(date)
    brand = Column(String)

    owner = relationship("User", back_populates="items")
