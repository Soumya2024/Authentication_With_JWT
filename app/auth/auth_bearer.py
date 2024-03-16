
#The goal of this file is to check whether the reques tis authorized or not [ verification of the proteced route]
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .auth_handler import decodeJWT


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid






# from fastapi import Request, HTTPException
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from .jwt_handler import decodeJWT

# class jwtBearer(HTTPBearer):
#     # def __init__(self, auto_error: bool = True):
#     #     super().__init__()
#     #     self.auto_error = auto_error
#     def __init__(self, auto_Error : bool = True):
#         super(jwtBearer, self).__init__()
#         self.auto_Error=auto_Error
        
#     async def __call__(self, request : Request):
#         credentials : HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
#         if not credentials:
#             if not credentials.scheme == "Bearer":
#                 raise HTTPException(status_code = 403, details = "Invslid or Experied Token")
#             return credentials.credentials
#         else:
#             raise HTTPException(status_code = 403, details = "Invalid or Expired Token ")
        
#     def verify_jwt(self, jwtoken : str):
#         isTokenValid : bool = False
#         payload = decodeJWT(jwtoken)
#         if payload:
#             isTokenValid = True
#         return isTokenValid


# from fastapi import Request, HTTPException
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from .jwt_handler import decodeJWT

# class jwtBearer(HTTPBearer):
#     def __init__(self, auto_error: bool = True):
#         super().__init__()
#         self.auto_error = auto_error
        
#     async def __call__(self, request: Request):
#         credentials: HTTPAuthorizationCredentials = await super().__call__(request)
#         if credentials and credentials.scheme == "Bearer":
#             return credentials.credentials
#         elif self.auto_error:
#             raise HTTPException(status_code=401, detail="Invalid or expired token")
#         else:
#             return None

#     def verify_jwt(self, jwtoken: str):
#         payload = decodeJWT(jwtoken)
#         if payload:
#             return payload
#         else:
#             return None





#The goal of this file is to check whether the reques tis authorized or not [ verification of the proteced route]
# from fastapi import Request, HTTPException
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# from .jwt_handler import decodeJWT


# class JWTBearer(HTTPBearer):
#     def __init__(self, auto_error: bool = True):
#         super(JWTBearer, self).__init__(auto_error=auto_error)

#     async def __call__(self, request: Request):
#         credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
#         if credentials:
#             if not credentials.scheme == "Bearer":
#                 raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
#             if not self.verify_jwt(credentials.credentials):
#                 raise HTTPException(status_code=403, detail="Invalid token or expired token.")
#             return credentials.credentials
#         else:
#             raise HTTPException(status_code=403, detail="Invalid authorization code.")

#     def verify_jwt(self, jwtoken: str) -> bool:
#         isTokenValid: bool = False

#         try:
#             payload = decodeJWT(jwtoken)
#         except:
#             payload = None
#         if payload:
#             isTokenValid = True
#         return isTokenValid



