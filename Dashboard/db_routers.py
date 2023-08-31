from fastapi import APIRouter,Depends,status
import Services.schemas as schemas
import Services.database as database
import Services.auth2 as auth2

from sqlalchemy.orm import Session
from typing import List,Annotated
from . import db_business

router = APIRouter(

prefix="/api/v1/dashboards",
tags=['Dashboards'])


@router.get("/maindash/data/")#response_model=List[schemas.CustomerbyType]
async def dashboardata(db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
  # print(db_business.dashboardData(db,current_user))
   return db_business.dashboardData(db,current_user)