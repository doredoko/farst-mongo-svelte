from fastapi import APIRouter,HTTPException,Depends
from app.model.data.user import User

from beanie import PydanticObjectId
from depends import sample_depends

userRouter = APIRouter()

@userRouter.get("")
async def retrieve_a_user_by_user_id(userId: PydanticObjectId):
    user = await User.get(userId)
    if user is None:
        raise HTTPException(status_code=404,
            etail="User not found")
    return user

@userRouter.post("",response_model=User,
dependencies=[Depends(sample_depends)])
async def post_a_user(body: User):
    await body.create()
    return body

@userRouter.patch("",response_model=User)
async def post_a_user(body:  User.UserRegister):
    user = await User(userName=body.userName).get(body.id)
    user.firstName = body.firstName
    user.lastName = body.lastName
    user.userName = body.userName
    user.address = user.address
    user.local = user.local
    user.preRegister = False
    user.updatedAd = body.updatedAd
    await user.save_changes()
    return user

