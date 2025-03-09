from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///moringa.db"

engine = create_engine(DATABASE_URL)
Mysession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = Mysession()
    try:
        yield db
    finally:
        db.close()
