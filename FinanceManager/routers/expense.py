from fastapi import APIRouter,Depends,status
#from .. import schemas,database,auth2
import Services.auth2 as auth2
import Services.models as models
import Services.schemas as schemas
import Services.database as database

from sqlalchemy.orm import Session
from typing import List,Annotated
from ..repository import expense

router = APIRouter(

prefix="/api/v1/finance",
tags=['Manage Expenses']

)

@router.post("/addexpense",)
async def CreateExpeses(request:schemas.Expense,db:Session=Depends(database.get_db),status_code=status.HTTP_201_CREATED,current_user:schemas.User= Depends(auth2.get_current_user)):
    return expense.CreateExpeses(db,request,current_user)
 
@router.get("/allexpenses/",response_model=List[schemas.showExpensebyUser])
async def ListAllexpense(db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
   return expense.ListAllexpense(db,current_user)


@router.get("/allexpenses/{usr_id}",response_model=List[schemas.showExpensebyUser])
async def ListAllexpense(usr_id:str,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
   return expense.ListAllexpenseByUser(db,usr_id)


@router.get("/{id}",response_model=schemas.showExpense)
async def showExpense(id:str,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
    return expense.showExpense(id,db)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def DeleteExpense(id:str,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
    return expense.DeleteExpense(id,db)

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED,)
async def updateExpense(id:str,request: schemas.Expense,db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
    return expense.UpdateExpense(id,db,request)



#Revenue Mangamement

@router.post("/addrevenue",)
async def CreateRevenue(request:schemas.Revenue,db:Session=Depends(database.get_db),status_code=status.HTTP_201_CREATED,current_user:schemas.User= Depends(auth2.get_current_user)):
    return expense.CreateRevenue(db,request,current_user)


@router.get("/allrevenues/",response_model=List[schemas.ListRevenues])
async def ListAllrevenues(db:Session=Depends(database.get_db),current_user:schemas.User= Depends(auth2.get_current_user)):
   return expense.ListAllrevenues(db,current_user)
