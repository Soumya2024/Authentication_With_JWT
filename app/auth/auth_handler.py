# #This file is responsible fot signing, encodig, decoding and returning JWTs.abs

# import time
# import jwt

# from decouple import config
# # Use config() function to access environment variables


# JWT_SECRET = config("secret")
# JWT_ALGORITHM = config("algorithm")

# # Funrtion returns the generated Tokens (JWTs)
# def token_response(token: str):
#     return{
#         "access token" : token
#     }
    

# # Function used for signing the JWT String
# def signJWT(userID : str):
#     payload = {
#         "userID" : userID,
#         "expiry" : time.time() + 600
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm = JWT_ALGORITHM)
#     return token_response(token)


# def decodeJWT(token: str):
#     try:
#         decode_token = jwt.decode(token, JWT_SECRET, algorithm = JWT_ALGORITHM)
#         return decode_token if decode_token['expires'] >= time.time() else None
#     except:
#         return{}







# import time
# import jwt
# from decouple import config

# JWT_SECRET = config("SECRET")
# JWT_ALGORITHM = config("ALGORITHM")

# # Function returns the generated token response
# def token_response(token: str):
#     return {
#         "access_token": token
#     }

# # Function used for signing the JWT string
# def signJWT(userID: str):
#     payload = {
#         "userID": userID,
#         "expiry": time.time() + 600  # Token expires in 10 minutes
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
#     return token_response(token)

# def decodeJWT(token: str):
#     try:
#         decode_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
#         return decode_token if decode_token['expiry'] >= time.time() else None
#     except jwt.ExpiredSignatureError:
#         # Token has expired
#         return None
#     except jwt.InvalidTokenError:
#         # Token is invalid
#         return None














# This file is responsible for signing , encoding , decoding and returning JWTS
import time
from typing import Dict

import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {
        "access_token": token
    }

# function used for signing the JWT string
def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
