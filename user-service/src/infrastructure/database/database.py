from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///evergreen.db'

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
