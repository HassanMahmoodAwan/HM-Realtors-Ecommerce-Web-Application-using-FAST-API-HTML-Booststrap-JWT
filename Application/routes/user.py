from fastapi import APIRouter
from __init__ import Schema

router = APIRouter(
    prefix = '/user',
    tags=['Users']
)

# === All Users ===
@router.get('/')
def all_users():
    return 'All user'

# === User at ID ===
@router.get('/{id}')
def get_user(id):
    return f'User of ID {id}'
    
# === Register new User ===    
@router.post('/')
def register_user(request: Schema.User):
    return request