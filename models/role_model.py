from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(String)
    description = Column(String)