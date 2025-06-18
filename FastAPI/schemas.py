from pydantic import BaseModel

class Signup(BaseModel):
    username: str
    password: str
    cpassword: str

class Signin(BaseModel):
    username: str
    password: str

class DeleteData(BaseModel):
    id: int
    username: str