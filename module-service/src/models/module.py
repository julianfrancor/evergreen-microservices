from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Module(Base):
    __tablename__ = 'modules'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    module_type = Column(Integer)