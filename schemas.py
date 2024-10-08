from pydantic import BaseModel
from typing import Optional
class UserBase(BaseModel):
    email: str

    class Config:
        from_attributes = True  # Update this from orm_mode

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True  # Update this from orm_mode

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True