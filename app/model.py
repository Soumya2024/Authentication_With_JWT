# from pydantic import BaseModel, Field, EmailStr


# class PostSchema(BaseModel):
#     id : int = Field(default=None)
#     title : str = Field(default=None)
#     content : str = Field(default=None)
#     class Config:
#         schema_extra = {
#             "post_demo" : {
#                 "title" : "some title about animals ",
#                 "content" : "some content about animals "
#             }
#         }
        
        

# class UserSchema(BaseModel):
#     fullname: str = Field(defaul = None)
#     email : EmailStr = Field(default = None)
#     password : str = Field(default = None)
#     class Config:
#         the_schema = {
#             "user_demo":{
#                     "name" : "Soumya",
#                     "email" : "help@soumya.com",
#                     "password" : "123"
#                 }
#         }
        
# class UserLoginSchema(BaseModel):
#     email : EmailStr = Field(default = None)
#     password : str = Field(default = None)
#     class Config:
#         the_schema = {
#             "user_demo":{
#                     "email" : "help@soumya.com",
#                     "password" : "123"
#                 }
#         }
        







from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
                "content": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens...."
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Joe Doe",
                "email": "joe@xyz.com",
                "password": "any"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@xyz.com",
                "password": "any"
            }
        }
