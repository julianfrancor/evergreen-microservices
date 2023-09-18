from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infrastructure.database.models.user_model import Base

DATABASE_URL = 'sqlite:///evergreen.db'

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
