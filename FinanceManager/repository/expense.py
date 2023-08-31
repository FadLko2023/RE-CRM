from fastapi import Depends,status,HTTPException
#from ...Services import models,schemas
import Services.models as models
import Services.schemas as schemas
from sqlalchemy.orm import Session
from typing import List

def CreateExpeses(db:Session,request:schemas.Expense,user:schemas.User):
    new_request=models.Expense(Exp_Type=request.Exp_Type,Particulars=request.Particulars,Payee=request.Payee,
                           Ammount=request.Ammount,Payment_Mode=request.Payment_Mode,Exp_Date=request.Exp_Date,user_id=user.id,Reference=request.Reference,
                           Description=request.Description)
    #new_request=models.Expense(request)
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

def ListAllexpense(db:Session, Curr_user:schemas.User):
    all_expense=db.query(models.Expense).filter(models.Expense.user_id==Curr_user.id).all()
    return all_expense

def ListAllexpenseByUser(db:Session,Curr_user:schemas.User):
    all_expense=db.query(models.Expense).filter(models.Expense.user_id==Curr_user.id).all()
    return all_expense

def showExpense(id:str,db:Session):
    show_expense=db.query(models.Expense).filter(models.Expense.id==id).first()
    if not show_expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Expense for id: {id} not found")
    return show_expense

def DeleteExpense(id:str,db:Session):
    records=db.query(models.Expense).filter(models.Expense.id==id)
    if not records.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"this id: {id} not found")
    
    records.delete(synchronize_session=False)
    db.commit()
    return {"message":"deleted"}

def UpdateExpense(id:str,db:Session,request: schemas.Expense):
    records=db.query(models.Expense).filter(models.Expense.id==id)
    if not records.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"this id: {id} not found")

    records.update(request.dict())
    db.commit()
    return "updated" 



# Revenue management

def CreateRevenue(db:Session,request:schemas.Revenue,current_user:schemas.User):
    new_request=models.RevenueTransaction(
        Type=request.Type,  # Seller's Comission, Buyer's Commission, Others
        Customer_Id=request.Customer_Id,
        PropertyId=request.PropertyId,
        SalePrice=request.SalePrice,
        Closing_date=request.Closing_date,
        PercentCommission=request.PercentCommission,
        GrossRevenue=request.GrossRevenue,
        BrokerShare=request.BrokerShare,
        BrokerCredit=request.BrokerCredit,
        CustomerShare=request.CustomerShare,
        CustomeCredit=request.CustomeCredit,
        TC_Share=request.TC_Share,
        TC_Credits=request.TC_Credits,
        Other_Credits=request.Other_Credits,
        NetRevenue=request.NetRevenue,
        user_id=current_user.id)

    
    #new_request=models.Expense(request)
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request


def ListAllrevenues(db:Session,current_user:schemas.User):
    all_revenues=db.query(models.RevenueTransaction).filter(models.RevenueTransaction.user_id==current_user.id).all()
    return all_revenues
