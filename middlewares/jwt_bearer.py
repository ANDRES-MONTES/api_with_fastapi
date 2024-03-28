
from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import create_token, decode_string



class JWTBearer(HTTPBearer):
    async def __call__(self, request:Request):
        auth =  await super().__call__(request)
        data = decode_string(auth.credentials)
        if data['email'] != 'admin@gmail.com':
            raise HTTPException(status_code =403, detail='credenciales invalidas')
        
