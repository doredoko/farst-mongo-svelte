from fastapi import APIRouter,HTTPException
from app.model.data.ticket import Ticket
from beanie import PydanticObjectId

ticketRouter = APIRouter()

@ticketRouter.get("/list",response_model=list[Ticket])
async def retrive_tickets(
    skip: int=0,
    limit: int = 30,
    userId: PydanticObjectId = None
):
    if(userId is None):
        return(
            await Ticket.find_all()
            .skip(skip)
            .limit(limit)
            .sort(-Ticket.createdAt)
            .to_list()
        )
    else:
        return (
            await Ticket.find_many(
           {"authorUserId": userId}
        )
        .sort(-Ticket.createdAt)
        .skip(skip)
        .limit(limit)
        .to_list()
        )
        
@ticketRouter.patch("")
async def update_ticket(
    tiketId: PydanticObjectId,
    title:str = None,
    body:str = None
):
 if(title is None and body is None ):
     raise HTTPException(status_code=422,
        detail="body or title is required")
 if(body is None):
     if(len(body)==0):
         raise HTTPException(status_code=422,
        detail='body is required')
 ticket = await Ticket.get(tiketId)
 if tiketId is None :
     raise HTTPException(status_code=400,
        detail="Ticket not found")
 if(title is not None):
     ticket.title = title if len(title) !=0 else None
 if(body is not None):
     ticket.body = body
 await ticket.save_changes()
 return ticket
