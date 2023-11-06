from beanie import Document
from datetime import datetime
from beanie import PydanticObjectId,Indexed
from typing import Optional

class Ticket(Document):
    title: str=None
    body: str
    authorId: Indexed(PydanticObjectId)
    referTicket: Indexed(PydanticObjectId) = None
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    
    class Settings:
        use_sate_management = True
        
    class Config:
        schema_extra = {
            "examole": {
                "title": "Taro",
                "body": "Ticket",
                "authorUserId": "T.T"
            }
        }