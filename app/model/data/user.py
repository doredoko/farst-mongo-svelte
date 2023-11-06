from pydantic import validator,BaseModel
from app.model.common import LOCATE_CHOICES
from beanie import Document
from datetime import datetime

class User(Document):
    firstName: str = None
    lastName: str = None
    userName: str
    address: int = None
    preRegister: bool = None
    locate: str ="JPN"
    created_at: datetime = None
    updated_at: datetime = None
    deleted_at: datetime = None
    
    @validator("created_at",pre=True,always=True)
    def insertCreatedAt(cls,v):
        return v or datetime.utcnow()
    
    class Settings:
        user_state_management = True
        
    class UserRegister(BaseModel):
        firstName: str
        lastName: str
        userName: str
        address: int
        locate: str ="JPN"
        
    class Config:
        schema_extra = {
            "example":{
                "firstName": "Taro",
                "lastName": "Ticket",
                "userName": "T.T",
                "address": "1234567",
                "locate": "JPN"
            }
        }