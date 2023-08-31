from fastapi import APIRouter,Depends,status,HTTPException
#from .. import schemas,database,auth2
import Services.auth2 as auth2
import Services.models as models
import Services.schemas as schemas
import Services.database as database

from sqlalchemy.orm import Session
from typing import List,Annotated

def AddProperty(db:Session,request:schemas.Properties,user:schemas.User):
    new_request=models.Property(
        
        Trasaction_Type= request.Trasaction_Type,
        CustomerId= request.CustomerId,
        Property_Address= request.Property_Address,
        Property_Type= request.Property_Type,
        Property_Ocuupancy= request.Property_Ocuupancy,
        MLS_Id= request.MLS_Id,
        Zpid= request.Zpid,
        ListPrice= request.ListPrice,
        SalePrice= request.SalePrice,
        Escrow_Open= request.Escrow_Open,
        Escrow_Close= request.Escrow_Close,
        ListingAgent= request.ListingAgent,
        BuyersAgent= request.BuyersAgent,
        Status= request.Status,
        user_id=user.id
    )
 
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request


def ListAllProperties(db:Session, Curr_user:schemas.User):
    all_expense=db.query(models.Property).filter(models.Property.user_id==Curr_user.id).all()
    return all_expense


def viewProperty(id:int,db:Session,current_user:schemas.User):
    PrpertyInfo=db.query(models.Property).filter(models.Property.user_id==current_user.id, models.Property.CustomerId==id).all()
    return PrpertyInfo


def DeleteProperty(id:int,db:Session):
    records=db.query(models.Property).filter(models.Property.id==id)
    if not records.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"this id: {id} not found")
    records.delete(synchronize_session=False)
    db.commit()
    return {"message":"deleted"}

def UpdateProperty(id:int,db:Session,request: schemas.Properties):
    records=db.query(models.Property).filter(models.Property.id==id)
    if not records.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"this id: {id} not found")

    records.update(request.dict())
    db.commit()
    return "updated" 