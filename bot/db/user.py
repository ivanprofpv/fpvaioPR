"""
Model user
"""

import datetime

from sqlalchemy import Column, Integer, VARCHAR, DATE

from .base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    # telegram user id
    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)

    # telegram user name
    username = Column(VARCHAR(32), unique=False, nullable=True)

    # user registration date in bot
    reg_date = Column(DATE, default=datetime.date.today())

    # user last update date
    upd_date = Column(DATE, onupdate=datetime.date.today())

    def __str__(self) -> str:
        return f'<User: {self.user_id}'