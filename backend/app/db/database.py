from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://arkabera@localhost/arka_teaches"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# DATABASE DEPENDENCY
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()