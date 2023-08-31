from fastapi import APIRouter,Depends,status
import Services.schemas as schemas
import Services.database as database
import Services.auth2 as auth2

from sqlalchemy.orm import Session
from typing import List,Annotated
from ..cm_business import customers

router = APIRouter(

prefix="/api/v1/customers",
tags=['Manage Customers']

)

@router.post("/addcustomer")
async def addcustomers(request:schemas.CreateCustomer,db:Session=Depends(database.get_db),status_code=status.HTTP_201_CREATED,current_user:schemas.User= Depends(auth2.get_current_user)):
    return customers.addcustomer(db,request,current_user)

@router.get("/allcustomer",response_model=List[schemas.showCustomerList])#List[schemas.CustomerFullName])#
async def getAllCustomers(db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
   return customers.getAllCustomers(db,current_user)

@router.get("/allcustomerList",response_model=List[schemas.CustomerFullName])
async def getAllCustomers(db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
   return customers.getAllCustomers(db,current_user)    

@router.get("/customerDetails/{id}",response_model="")
async def getCustomerDetails(id:int,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
    return customers.getCustomerDetails(id,db,current_user)

@router.get("/customerAddress/{id}",response_model=List[schemas.showAddress])
async def getCustomerAddress(id:int,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
    return customers.getCustomerAddress(id,db,current_user)


@router.put("/updateCustomer/{id}",status_code=status.HTTP_202_ACCEPTED,)
async def updateCustomer(id:int,request: schemas.CreateCustomer,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
    return customers.UpdateCustomer(id,db,request)


@router.delete("/deleteCustomer/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def DeleteCustomer(id:str,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
    return customers.DeleteCustomer(id,db)