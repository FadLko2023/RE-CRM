from datetime import datetime, timedelta
from typing import Annotated
from jose import JWTError, jwt
#from .schemas import TokenData,User
from Services.schemas import TokenData,User
from sqlalchemy.orm import Session
from Services import models


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 40


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verifyToken(token:str,credentials_exception,db:Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        Email_Id: str = payload.get("sub")
        if Email_Id is None:
            raise credentials_exception
        token_data = TokenData(Email_Id=Email_Id)
    except JWTError:
        raise credentials_exception
    user=db.query(models.User).filter(models.User.Email_Id==Email_Id).first()
    if user is None:
        raise credentials_exception
    return user
    


  