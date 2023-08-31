from fastapi import FastAPI
from Services import models
from Services.database import engine
from FinanceManager.routers import expense #authentication #users,
from  UserManager.um_routers import users,authentication
from fastapi.middleware.cors import CORSMiddleware
from CustomerManager.cm_routers import customers
from ProductManager.pm_routers import pm_routers
from Dashboard import db_routers

models.Base.metadata.create_all(bind=engine)
app=FastAPI()

origins=[
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

app.include_router(authentication.router)
app.include_router(expense.router)
app.include_router(users.router)
app.include_router(customers.router)
app.include_router(pm_routers.router)
app.include_router(db_routers.router)

@app.get("/api")
async def root():
    return {"message": "This is from api"} 
