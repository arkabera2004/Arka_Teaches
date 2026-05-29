from sqlalchemy.orm import Session
from app.db.models import User


def create_user(db: Session, user_data):

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        learning_level=user_data.learning_level,
        daily_study_hours=user_data.daily_study_hours
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_all_users(db: Session):

    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):

    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: int):

    user = db.query(User).filter(User.id == user_id).first()

    if user:
        db.delete(user)
        db.commit()

    return user
# def update_user(db, user_id, updated_user):

#     user = db.query(User).filter(User.id == user_id).first()

#     if not user:
#         return None

#     user.name = updated_user.name
#     user.email = updated_user.email
#     user.learning_level = updated_user.learning_level
#     user.daily_study_hours = updated_user.daily_study_hours

#     db.commit()
#     db.refresh(user)

#     return user    
def update_user(
    db,
    user_id,
    updated_user
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return None

    user.name = updated_user.name
    user.email = updated_user.email
    user.learning_level = updated_user.learning_level
    user.daily_study_hours = updated_user.daily_study_hours

    db.commit()
    db.refresh(user)

    return user