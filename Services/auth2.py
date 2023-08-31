from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from .token import verifyToken
from sqlalchemy.orm import Session
from .database import get_db

from fastapi import HTTPException,Depends,status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/authentication/loginuser")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],db:Session=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verifyToken(token,credentials_exception,db)
  
