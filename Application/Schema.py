from pydantic import BaseModel

class User(BaseModel):
    First_Name: str
    Last_Name: str
    Email: str
    Password: str


class Product(BaseModel):
    Name: str
    Brand: str
    Category: str
    Qty: int
    Price: float
    M_date: str
    E_date: str