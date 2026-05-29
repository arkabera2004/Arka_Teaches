from fastapi import FastAPI

from app.api.routes import user
from app.db.database import engine
from app.db.models import Base



app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Arka Teaches Backend Running"}