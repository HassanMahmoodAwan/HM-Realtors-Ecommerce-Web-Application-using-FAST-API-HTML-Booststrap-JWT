from fastapi import APIRouter, status, Depends
from __init__ import Schema, Models, Database
from sqlalchemy.orm import Session



router = APIRouter(
    prefix = '/user',
    tags=['Users']
)

# === All Users ===
@router.get('/')
def all_users():
    return 'All user'

# === User at ID ===
@router.get('/{id}', status_code=200)
def get_user(id):
    return f'User of ID {id}'
    
# === Register new User ===    
@router.post('/')
def register_user(request: Schema.User, db: Session = Depends(Database.get_db)):
    new_user = Models.User(First_Name = request.First_Name, Last_Name = request.Last_Name, Email =  request.Email, Password = request.Password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return f'User registered Successfully \n {request}'