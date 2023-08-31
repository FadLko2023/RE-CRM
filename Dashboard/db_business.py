from fastapi import APIRouter,Depends,status,HTTPException
#from .. import schemas,database,auth2
import Services.auth2 as auth2
import Services.models as models
import Services.schemas as schemas
import Services.database as database
from sqlalchemy import func,funcfilter
from sqlalchemy.orm import Session
from typing import List,Annotated
import json



def dashboardData(db:Session,current_user:schemas.User):
     Customer_by_type=db.query(models.Customer.Type, funcfilter(func.count(models.Customer.Type),models.Customer.user_id==current_user.id)).group_by(models.Customer.Type).all()
     Expense_by_type=db.query(models.Expense.Exp_Type, funcfilter(func.sum(models.Expense.Ammount),models.Expense.user_id==current_user.id)).group_by(models.Expense.Exp_Type).all()
     Property_by_type=db.query(models.Property.Trasaction_Type, funcfilter(func.count(models.Property.Trasaction_Type),models.Property.user_id==current_user.id)).group_by(models.Property.Trasaction_Type).all()
     #Customer_by_type=Customer_by_type
     
     Total_Customer=db.query(funcfilter(func.count(models.Customer.Type),models.Customer.user_id==current_user.id)).all()[0][0]
     Total_Expennse=db.query(funcfilter(func.sum(models.Expense.Ammount),models.Expense.user_id==current_user.id)).all()[0][0]
     Total_Proeprties=db.query(funcfilter(func.count(models.Property.Trasaction_Type),models.Property.user_id==current_user.id)).all()[0][0]

     print(Total_Customer)

     dt=[]
     
     date_db=[]
     
     for rec in Customer_by_type:
         dt.append({"Type":rec[0],"Count":rec[1]})
    
     date_db.append(dt)
  
     dt=[]
     for rec in Expense_by_type:
         dt.append({"Type":rec[0],"Count":rec[1]})
      
     date_db.append(dt)

     dt=[]
     for rec in Property_by_type:
         dt.append({"Type":rec[0],"Count":rec[1]})
      
     date_db.append(dt)

     date_db.append([{"Total":"Customer","Value":Total_Customer},{"Total":"Properties","Value":Total_Proeprties},{"Total":"Expense","Value":Total_Expennse}])
     
     return date_db