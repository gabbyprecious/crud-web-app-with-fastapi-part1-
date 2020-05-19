from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    first_name: str
    last_name: str 
    email: str
    password: str

class User(UserBase):
    id: int
    password: str
    
    class Config:
        orm_mode = True
        