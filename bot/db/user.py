from sqlalchemy import Column, Integer, VARCHAR, DATE

from .base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    # telegram user id
    user_id = Column(Integer, unique=True, nullable=False)

    # telegram user name
    username = Column(VARCHAR(32), unique=False, nullable=True)

    # user registration date in bot
    reg_date = Column()

    # user last update date
    upd_date = Column()

    def __str__(self) -> str:
        return f'<User: {self.user_id}'