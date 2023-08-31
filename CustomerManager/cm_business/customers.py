from fastapi import Depends,status,HTTPException

import Services.models as models
import Services.schemas as schemas
import Services.database as database
import Services.auth2 
from sqlalchemy.orm import Session
from typing import List


def addcustomer(db:Session,request:schemas.CreateCustomer,user:schemas.User):
    ctmr=request.Customer
    add_customer=models.Customer(Type=ctmr.Type,First_Name=ctmr.First_Name,Last_Name=ctmr.Last_Name, Email_Id=ctmr.Email_Id,Phone_Number=ctmr.Phone_Number, Inception_Date=ctmr.Inception_Date, TimeLine=ctmr.TimeLine,
                                   Budget=ctmr.Budget, Funding_Source=ctmr.Funding_Source, Loan_status=ctmr.Loan_status, Percent_DownPayment=ctmr.Percent_DownPayment,user_id=user.id)
   
    #new_request=models.Expense(request)
    db.add(add_customer)
    db.commit()
    db.refresh(add_customer)

    cust_id=db.query(models.Customer).filter(models.Customer.First_Name==ctmr.First_Name,models.Customer.Last_Name==ctmr.Last_Name, models.Customer.Email_Id==ctmr.Email_Id).first().id

    addr=request.Address
    
    add_address=models.Address(Address_Line=addr.Address_Line,
                                City=addr.City,
                                State=addr.State,
                                PostalCode=addr.PostalCode,
                                Country=addr.Country,
                                Customer_Id=cust_id
                                )

    db.add(add_address)
    db.commit()
    db.refresh(add_address)
    
    requiremnt=request.Requirements

    add_requiremnt=models.PropertyRequirement(
                            LOB= requiremnt.LOB,
                            Construction= requiremnt.Construction,
                            Min_Sq_Footage= requiremnt.Min_Sq_Footage,
                            Occupancy_Type= requiremnt.Occupancy_Type,
                            Building_Age= requiremnt.Building_Age,
                            Bedrooms= requiremnt.Bedrooms,
                            Bathrooms= requiremnt.Bathrooms,
                            Condition= requiremnt.Condition,
                            Locality= requiremnt.Locality,
                            Is_School= requiremnt.Is_School,
                            School_District= requiremnt.School_District,
                            Customer_Id=cust_id
    )
    db.add(add_requiremnt)
    db.commit()
    db.refresh(add_requiremnt)

    return add_customer


def getAllCustomers(db:Session,Curr_user:schemas.User):
    all_customer=db.query(models.Customer).filter(models.Customer.user_id==Curr_user.id).all()
   # print(Curr_user.id)

    print(all_customer)
    return all_customer

def getCustomerDetails(id:int,db:Session,Curr_user:schemas.User):
    getCustomerInfo=db.query(models.Customer).filter(models.Customer.id==id,models.Customer.user_id==Curr_user.id).first()
    getCustomerAddress=db.query(models.Address).filter(models.Address.Customer_Id==id).first()
    getCustomerRequierments=db.query(models.PropertyRequirement).filter(models.PropertyRequirement.Customer_Id==id).first()

    return {
        "Customer":getCustomerInfo,
        "Address":getCustomerAddress,
        "Requirements":getCustomerRequierments
    }

def getCustomerAddress(id:int,db:Session,Curr_user:schemas.User):
    getCustomerAddress=db.query(models.Address).filter(models.Address.Customer_Id==id).first()
    return getCustomerAddress



def UpdateCustomer(id:int,db:Session,request:schemas.CreateCustomer):
    customers=db.query(models.Customer).filter(models.Customer.id==id)
    if not customers.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"this id: {id} not found")

    customers.update(request.Customer.dict())
    address=db.query(models.Address).filter(models.Address.Customer_Id==id)
    requirments=db.query(models.PropertyRequirement).filter(models.PropertyRequirement.Customer_Id==id)

    address.update(request.Address.dict())
    requirments.update(request.Requirements.dict())
    db.commit()
    return "updated" 


def DeleteCustomer(id:int,db:Session):
    customer=db.query(models.Customer).filter(models.Customer.id==id)
    if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"this id: {id} not found")
    
    customer.delete(synchronize_session=False)
   # db.commit()
    address=db.query(models.Address).filter(models.Address.Customer_Id==id)
    address.delete(synchronize_session=False)
    
    requirements=db.query(models.PropertyRequirement).filter(models.PropertyRequirement.Customer_Id==id)
    requirements.delete(synchronize_session=False)

    db.commit()

    return {"message":"deleted"}



