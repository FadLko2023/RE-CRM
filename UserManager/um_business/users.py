from fastapi import APIRouter,Depends,status,HTTPException
from Services import models,schemas,database
from UserManager.um_business import hashing
from sqlalchemy.orm import Session
from typing import List

from sqlalchemy import and_

async def CreateUser(db:Session,request:schemas.User):
    check_emailid=db.query(models.User).filter(models.User.Email_Id==request.Email_Id).first() 
    if check_emailid:
        raise HTTPException(status_code=status.HTTP_302_FOUND,detail=f"User with emailid {request.Email_Id} already exist")
    
    hassedPwd=hashing.Hash.bycrpt_pw(request.Password)
    new_request=models.User(First_Name=request.First_Name,Last_Name=request.Last_Name,Email_Id=request.Email_Id,Password=hassedPwd,
                            Company=request.Company,Date_created=request.Date_created, Role=request.Role)
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

def GetAllUsers(db:Session):
    all_users=db.query(models.User).all()
    return all_users


def showUser(id:str,db:Session,current_user):
    show_user=db.query(models.User).filter(and_(models.User.id==id ,models.User.Email_Id==current_user.Email_Id)).first()

    if not show_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User not logged in")
    return show_user

async def getCurrentUser(db:Session,current_user):
    show_user=db.query(models.User).filter(models.User.Email_Id==current_user.Email_Id).first()
    if not show_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User not logged in")
    return show_user



def getUser(emailid:str,db:Session):
    user=db.query(models.User).filter(models.User.Email_Id==emailid).first()
    return user