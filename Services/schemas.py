from enum import Enum
from datetime import date
from  pydantic import BaseModel
from typing import Optional,List

class ExpenseType(str,Enum):
    travel= "travel"
    entertainment="entertainment"
    advertisement="edvertisement"
    office="office"
    fees="fees"
    commission="commission"

class PaymentMode(str,Enum):
    CreditCard="Credit Card"
    BankTransfer="Bank Transfer"
    Cash="Cash"

class UserRole(str,Enum):
    Admin="Admin"
    User="General User"
    Other="Other"



class Expense(BaseModel):
    Exp_Type:str
    Particulars:str
    Payee:str
    Ammount:float
    Exp_Date:Optional[date]
    Payment_Mode:str
    Reference:str|None=None
    Description :str|None=None

class showExpensebyUser(Expense):
    id:int
    class Config:
        from_attributes=True


#User pydentic models

'''class User(BaseModel):
    First_Name:str
    Last_Name:str
    Email_Id:str
    Password:str
    Company:str
    Role:str
    Date_created:Optional[date]'''

class User(BaseModel):
    First_Name:str
    Last_Name:str
    Email_Id:str
    Password:str
    Company:str
    Role:UserRole
    Date_created:Optional[date]

class Profile(BaseModel):
    
    First_Name:str
    Last_Name:str
    Email_Id:str
    Title:str|None=None
    Company:str
    Certification:str|None=None
    Education:str|None=None
    Role:UserRole
    Image_Url:str|None=None
    Date_created:Optional[date]

class showProfile(BaseModel):
    id:int
    First_Name:str
    Last_Name:str
    Email_Id:str
    Title:str|None=None
    Role:UserRole
    Company:str
    Certification:str|None=None
    Education:str|None=None
    Image_Url:str|None=None
    Date_created:Optional[date]
    
  
    class Config:
        from_attributes=True

    

class showUser(BaseModel):
    id:int
    First_Name:str
    Last_Name:str
    Email_Id:str
    
    class Config:
        from_attributes=True

# Expenses Scehma
#Request pydentic schemas
class Expense(BaseModel):
    Exp_Type:str
    Particulars:str
    Payee:str
    Ammount:float
    Exp_Date:Optional[date]
    Payment_Mode:str
    Reference:str|None=None
    Description :str|None=None

# response pydantic schemas

class showExpense(BaseModel):
    id:int
    Payee:str
    Ammount:float
    owner:Profile

    class Config:
        from_attributes=True


class Login(BaseModel):
    Email_Id:str
    Password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    Email_Id: str | None = None


# Customer mananger schemas

class Address(BaseModel):   
    Address_Line:str
    City:str
    State:str
    PostalCode:str
    Country:str

class showAddress(Address):
    class Config:
        from_attributes=True


class PropertyRequirements(BaseModel):
    LOB:str
    Construction:str
    Min_Sq_Footage:str
    Occupancy_Type:str
    Building_Age:str
    Bedrooms:int
    Bathrooms:int
    Condition:str
    Locality:str
    Is_School:bool
    School_District:str


class Customer(BaseModel):
    Type:str
    First_Name:str
    Last_Name:str
    Email_Id:str
    Phone_Number:str
    Inception_Date:date
    TimeLine:str
    Budget:float
    Funding_Source:str
    Loan_status:bool
    Percent_DownPayment:float

class CreateCustomer(BaseModel):
    Customer:Customer
    Address:Address
    Requirements:PropertyRequirements


class showCustomerList(Customer):
    id:int
    class Config:
        from_attributes=True

class CustomerFullName(BaseModel):
    Type:str
    First_Name:str
    Last_Name:str
    id:int
    class Config:
        from_attributes=True



class Properties(BaseModel):

    Trasaction_Type:str
    CustomerId:int
    Property_Address:str
    Property_Type:str #Residential, Commercial, Industrial
    Property_Ocuupancy:str #Single Family, Townhome, Condo, Duplex
    MLS_Id:str
    Zpid:str
    ListPrice:float
    SalePrice:float
    Escrow_Open:date
    Escrow_Close:date
    ListingAgent:str
    BuyersAgent:str
    Status:str
    

class showProperties(BaseModel):
    id:int
    Trasaction_Type:str
    CustomerId:int
    Property_Address:str
    Property_Type:str #Residential, Commercial, Industrial
    Property_Ocuupancy:str #Single Family, Townhome, Condo, Duplex
    MLS_Id:str
    Zpid:str
    ListPrice:float
    SalePrice:float
    Escrow_Open:date
    Escrow_Close:date
    ListingAgent:str
    BuyersAgent:str
    Status:str

    class Config:
        from_attributes=True

class CustomerbyType(BaseModel):
    Type:str
    Count: int

    class Config:
        from_attributes=True

class Revenue(BaseModel):
    Type:str  # Seller's Comission, Buyer's Commission, Others
    Customer_Id:int
    PropertyId:int
    SalePrice:float
    Closing_date:date
    PercentCommission:float
    GrossRevenue:float
    BrokerShare:float
    BrokerCredit:float
    CustomerShare:float
    CustomeCredit:float
    TC_Share:float
    TC_Credits:float
    Other_Credits:float
    NetRevenue:float

class ListRevenues(Revenue):
    id:int

    class Config:
        from_attributes=True









