from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    name = Column(String)
    last_name = Column(String)
    user_type = Column(String)
    password = Column(String)
    status = Column(String)
