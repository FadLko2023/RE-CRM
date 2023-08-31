from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    
    def bycrpt_pw(password:str):
        return pwd_context.hash(password)
    

    def verifyPW(plain_pwd,hashd_pwd):
        return pwd_context.verify(plain_pwd,hashd_pwd)

