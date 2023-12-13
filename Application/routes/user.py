from fastapi import APIRouter, status, Depends, HTTPException
from __init__ import Schema, Models, Database, Hashing
from sqlalchemy.orm import Session



router = APIRouter(
    prefix = '/user',
    tags=['Users']
)

# === All Users ===
@router.get('/', status_code= 200)
def all_users(db: Session = Depends(Database.get_db)):
    all_users = db.query(Models.User).all()
    return all_users

# === User at ID ===
@router.get('/{ID}', status_code=200)
def get_user(ID):
    return f'User of ID {id}'
    
# === Register new User ===    
@router.post('/', status_code= 201)
def register_user(request: Schema.User, db: Session = Depends(Database.get_db)):
    hashed_password = Hashing.Hash.bcrypt(request.Password)
    new_user = Models.User(First_Name = request.First_Name, Last_Name = request.Last_Name, Email =  request.Email, Password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return f'User registered Successfully \n {request}'


# # === Delete Existing User ===
# @router.delete('/{ID}', status_code=204)
# def delete_user(ID, db: Session = Depends(Database.get_db)):
#     user = db.query(Models.User).filter(Models.User.ID == ID)
#     if not user.first():
#         raise HTTPException(status_code=404, 
#         detail=f'User with {ID} did not Exist')
    
#     user.delete(synchronize_session = False)
#     db.commit()
#     return f'User with ID: {ID} Deleted'