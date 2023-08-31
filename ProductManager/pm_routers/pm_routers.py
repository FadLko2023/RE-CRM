from fastapi import APIRouter,Depends,status
import Services.schemas as schemas
import Services.database as database
import Services.auth2 as auth2

from sqlalchemy.orm import Session
from typing import List,Annotated
from ..pm_business import pm_business

router = APIRouter(

prefix="/api/v1/products",
tags=['Manage Products']

)

@router.post("/addProperty")
async def AddProperty(request:schemas.Properties,db:Session=Depends(database.get_db),status_code=status.HTTP_201_CREATED,current_user:schemas.User= Depends(auth2.get_current_user)):
    return pm_business.AddProperty(db,request,current_user)


@router.get("/allproperties/",response_model=List[schemas.showProperties])
async def ListAllProperties(db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
   return pm_business.ListAllProperties(db,current_user)

@router.get("/viewProperty/{id}",response_model=List[schemas.showProperties])
async def viewProperty(id:int,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
   return pm_business.viewProperty(id,db,current_user)

@router.delete("/deleteProduct/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def DeleteProperty(id:int,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
    return pm_business.DeleteProperty(id,db)

@router.put("/updateProduct/{id}",status_code=status.HTTP_202_ACCEPTED,)
async def updateProperty(id:int,request: schemas.Properties,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
    return pm_business.UpdateProperty(id,db,request)