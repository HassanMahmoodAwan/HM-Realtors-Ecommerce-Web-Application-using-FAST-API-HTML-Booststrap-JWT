from fastapi import APIRouter, Depends, status
from __init__ import Database, Schema, Models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/products',
    tags=['Products']
)



# === Get All Products ===
@router.get('/', status_code= 200)
def all_products(db: Session = Depends(Database.get_db)):
    all_products = db.query(Models.Product).all()
    return all_products


# === Specific Product of {ID} ===
@router.get('/{id}')
def get_product(id):
    return f'All Products Here {id}'


# === Add Product in Inventory ===
