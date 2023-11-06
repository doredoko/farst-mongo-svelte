from fastapi import FastAPI
import motor
from beanie import init_beanie
from app.endpoint.user import userRouter
from app.endpoint.ticket import ticketRouter
from app.model.data.user import User
from app.model.data.ticket import Ticket
from fastapi.middleware.cors import CORSMiddleware
import os

app=FastAPI()

@app.on_event("startup")
async def app_init():
    db_url = os.environ.get("DB_URL")
    client = motor.motor_asyncio.AsyncIOMotorClient(db_url)
    await init_beanie(
    client.my_db,
    document_models=[User]
    ) 
    await init_beanie(client.questTicket,document_models=[User,Ticket])
app.include_router(userRouter,prefix="/user",tags=["User"])
app.include_router(ticketRouter,prefix="/ticket",tags=["Ticket"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#second