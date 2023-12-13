# ===== Developing ORM models for different Routes ======

from __init__ import Database
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import Relationship

Base = Database.Base

class User(Base):
    __tablename__ = 'Users Registeration'

    ID = Column(Integer, primary_key=True, index=True)
    First_Name = Column(String)
    Last_Name = Column(String)
    Email = Column(String)
    Password = Column(String)
    
    
class Product(Base):
    __tablename__ = 'Create Product'

    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Brand = Column(String)
    Category = Column(String)
    Qty = Column(Integer)
    Price = Column(Float)
    M_date = Column(String)
    E_date = Column(String)