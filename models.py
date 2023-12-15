from pydantic import BaseModel

class UserCreate(BaseModel):
    mobile_number: str
    username: str

class OTPVerification(BaseModel):
    otp: str
    password: str

class UserDetails(BaseModel):
    username: str
    name: str
    address: str
    hometown: str
    blood_group: str