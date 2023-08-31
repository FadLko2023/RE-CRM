from uuid import uuid4
from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float,Date,Text
from sqlalchemy.orm import relationship
from .schemas import ExpenseType

class Expense(Base):
    __tablename__="expenses"

    id=Column(Integer,primary_key=True)  #Column('id',Text(length=36),default=lambda: str(uuid4()), primary_key=True)
    Exp_Type=Column(String)
    Particulars=Column(String)
    Payee=Column(String,nullable=True)
    Ammount=Column(Float)
    Exp_Date=Column(Date,nullable=True)
    Payment_Mode=Column(String)
    Reference=Column(String,nullable=True )
    Description=Column(String,nullable=True)

    user_id=Column(Integer,ForeignKey("users.id"))

    owner=relationship("User", back_populates="expenses")

    #__allow_unmapped__ = True


class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True) #Column('id',Text(length=36),default=lambda: str(uuid4()), primary_key=True)
    First_Name=Column(String)
    Last_Name=Column(String)
    Email_Id=Column(String)
    Company=Column(String)
    Title=Column(String,nullable=True)
    Certification=Column(String,nullable=True)
    Education=Column(String,nullable=True)
    Role=Column(String)
    Image_Url=Column(String,nullable=True)
    Date_created=Column(Date)
    Password=Column(String)

    expenses=relationship("Expense",back_populates="owner")

    customers=relationship("Customer",back_populates="owner")

    properties=relationship("Property",back_populates="owner")

    revenue=relationship("RevenueTransaction", back_populates="owner")


#Customer Management

class Customer(Base):
    __tablename__="customers"
    id=Column(Integer,primary_key=True)
    Type=Column(String)
    First_Name=Column(String)
    Last_Name=Column(String)
    Email_Id=Column(String)
    Phone_Number=Column(String)
    Inception_Date=Column(Date)
    TimeLine=Column(String)
    Budget=Column(Float)
    Funding_Source=Column(String)
    Loan_status=Column(Boolean)
    Percent_DownPayment=Column(Float)
    user_id=Column(Integer,ForeignKey("users.id"))

    owner=relationship("User", back_populates="customers")

class Address(Base):
    __tablename__="addresses"
    id=Column(Integer,primary_key=True)
    Customer_Id=Column(String,ForeignKey("customers.id"))
    Address_Line=Column(String)
    City=Column(String)
    State=Column(String)
    PostalCode=Column(String)
    Country=Column(String)

class PropertyRequirement(Base):
    __tablename__="property_requirements"
    id=Column(Integer,primary_key=True)
    Customer_Id=Column(String,ForeignKey("customers.id"))
    LOB=Column(String)
    Construction=Column(String)
    Min_Sq_Footage=Column(String,nullable=True)
    Occupancy_Type=Column(String)
    Building_Age=Column(String)
    Bedrooms=Column(Integer)
    Bathrooms=Column(Integer)
    Condition=Column(String)
    Locality=Column(String)
    Is_School=Column(Boolean)
    School_District=Column(String)



class RevenueTransaction(Base):
    __tablename__="revenue"
    id=Column(Integer,primary_key=True)
    Type=Column(String)  # Seller's Comission, Buyer's Commission, Others
    Customer_Id=Column(Integer,ForeignKey("customers.id"))
    PropertyId=Column(Integer)
    SalePrice=Column(Float)
    Closing_date=Column(Date)
    PercentCommission=Column(Float)
    GrossRevenue=Column(Float)
    BrokerShare=Column(Float)
    BrokerCredit=Column(Float)
    CustomerShare=Column(Float)
    CustomeCredit=Column(Float)
    TC_Share=Column(Float)
    TC_Credits=Column(Float)
    Other_Credits=Column(Float)
    NetRevenue=Column(Float)

    user_id=Column(Integer,ForeignKey("users.id"))

    owner=relationship("User", back_populates="revenue")


class Property(Base):
    __tablename__="properties"
    id=Column(Integer,primary_key=True)
    Trasaction_Type=Column(String)  #Sellers, Buyers
    CustomerId=Column(Integer,ForeignKey("customers.id"))
    Property_Address=Column(String)
    Property_Type=Column(String) #Residential, Commercial, Industrial
    Property_Ocuupancy=Column(String) #Single Family, Townhome, Condo, Duplex
    MLS_Id=Column(String)
    Zpid=Column(String)
    ListPrice=Column(Float)
    SalePrice=Column(Float)
    Escrow_Open=Column(Date)
    Escrow_Close=Column(Date)
    ListingAgent=Column(String)
    BuyersAgent=Column(String)
    Status=Column(String)
    user_id=Column(Integer,ForeignKey("users.id"))

    owner=relationship("User", back_populates="properties")

    














