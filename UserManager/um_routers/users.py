from fastapi import APIRouter,Depends
#from .. import models,schemas,database,auth2,token

import Services.schemas as schemas
import Services.database as database
import Services.auth2 as auth2
from UserManager.um_business import token

from sqlalchemy.orm import Session
from typing import List

from UserManager.um_business import users

router = APIRouter(
    
prefix="/api/v1/users",
tags=['Manage Users']

)

@router.post("/createuser")
async def CreateUser(request:schemas.User, db:Session=Depends(database.get_db)):
    new_user=await users.CreateUser(db,request)
    access_token = token.create_access_token(data={"sub": request.Email_Id})#, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
   
@router.get("/allusers",response_model=List[schemas.showUser])
async def getAllUsers(db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
    print(current_user.Email_Id)
    return users.GetAllUsers(db)

@router.get("/me",response_model=schemas.showProfile)
async def getCurrentUser(db:Session=Depends(database.get_db),current_user:schemas.Profile= Depends(auth2.get_current_user)):
    return await users.getCurrentUser(db,current_user)

@router.get("/{id}",response_model=schemas.showUser)
async def showUser(id:str,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
    return users.showUser(id,db,current_user)


