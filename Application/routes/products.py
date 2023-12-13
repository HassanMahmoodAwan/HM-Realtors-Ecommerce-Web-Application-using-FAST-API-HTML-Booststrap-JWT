from fastapi import APIRouter

router = APIRouter(
    prefix='/products',
    tags=['Products']
)


# === Get All Products ===
@router.get('/')
def all_products():
    return 'All Products Here'

# === Specific Product of {ID} ===
@router.get('/{id}')
def get_product(id):
    return f'All Products Here {id}'