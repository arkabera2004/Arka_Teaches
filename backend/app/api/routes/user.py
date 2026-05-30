from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.db.database import get_db

from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserUpdate
)

from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    delete_user,
    update_user
)
router = APIRouter()


@router.post("/users")
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    try:

        new_user = create_user(db, user)

        return {
            "message": "User created successfully",
            "user_id": new_user.id
        }

    except IntegrityError:

        db.rollback()

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )


@router.get("/users", response_model=list[UserResponse])
def fetch_users(
    db: Session = Depends(get_db)
):

    return get_all_users(db)


@router.get("/users/{user_id}")
def fetch_single_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = get_user_by_id(db, user_id)

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.delete("/users/{user_id}")
def remove_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = delete_user(db, user_id)

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }
@router.put("/users/{user_id}", response_model=UserResponse)
def modify_user(
    user_id: int,
    updated_user: UserUpdate,
    db: Session = Depends(get_db)
):
    try:

        user = update_user(
            db,
            user_id,
            updated_user
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return user

    except IntegrityError:

        db.rollback()

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
