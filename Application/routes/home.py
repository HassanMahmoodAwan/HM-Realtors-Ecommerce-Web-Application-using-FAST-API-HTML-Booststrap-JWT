from fastapi import APIRouter


router = APIRouter(
    tags=['Home Page']
)

@router.get('/')
def home():
    return 'This is home Page'