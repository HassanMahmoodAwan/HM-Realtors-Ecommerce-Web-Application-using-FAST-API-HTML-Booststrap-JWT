from pydantic import BaseModel

class User(BaseModel):
    First_Name: str
    Last_Name: str
    Email: str
    Password: str
