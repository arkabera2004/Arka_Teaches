from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):

    name: str = Field(..., min_length=2, max_length=100)

    email: EmailStr

    learning_level: str = Field(..., min_length=2, max_length=50)

    daily_study_hours: int = Field(..., ge=0, le=24)


class UserResponse(BaseModel):

    id: int
    name: str
    email: str
    learning_level: str
    daily_study_hours: int

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    learning_level: str
    daily_study_hours: int        