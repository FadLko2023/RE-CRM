from fastapi import APIRouter,Depends,HTTPException,status
import Services.schemas as schemas
import Services.database as database
import Services.auth2 as auth2
import Services.models as models

from UserManager.um_business import token,hashing
from sqlalchemy.orm import Session 
from fastapi.security import OAuth2PasswordRequestForm

from typing import Annotated


router = APIRouter(

prefix="/api/v1/authentication",
tags=['Authetication']
)

@router.post("/loginuser")
#async def login(request:schemas.Login,db:Session=Depends(database.get_db)):
async def login(request:Annotated[OAuth2PasswordRequestForm, Depends()],db:Session=Depends(database.get_db)):
    userid=db.query(models.User).filter(models.User.Email_Id==request.username).first()
    if not userid:
        raise HTTPException(status_code=status.HTTP_302_FOUND,detail=f"Invaid emailid or password")
    
    if not hashing.Hash.verifyPW(request.password,userid.Password):
        raise HTTPException(status_code=status.HTTP_302_FOUND,detail=f"Invaid emailid or password")
    #generate JTWT token and return it
   
   # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = token.create_access_token(data={"sub": userid.Email_Id})#, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer","user":userid.Email_Id,"First_Name":userid.First_Name}


''''
@router.post("/loginuser")
#async def login(request:schemas.Login,db:Session=Depends(database.get_db)):
async def login(request:Login,db:Session=Depends(database.get_db)):
    userid=db.query(models.User).filter(models.User.Email_Id==request.Email_Id).first()
    if not userid:
        raise HTTPException(status_code=status.HTTP_302_FOUND,detail=f"Invaid emailid or password")
    
    if not hashing.Hash.verifyPW(request.Password,userid.Password):
        raise HTTPException(status_code=status.HTTP_302_FOUND,detail=f"Invaid emailid or password")
    #generate JTWT token and return it

   # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(data={"sub": userid.Email_Id})#, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
    '''



