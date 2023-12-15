from fastapi import FastAPI
from models import UserCreate,OTPVerification,UserDetails
from userclass import UserManager


app = FastAPI()
user_manager = UserManager()
@app.post("/signup/")
async def signup(user_create: UserCreate):
    otp = user_manager.create_user(user_create)
    # Send OTP notification (replace with your actual notification logic)
    # send_otp_notification(user_create.mobile_number, otp)
    return {"message": "OTP sent successfully"}

@app.post("/verify-otp/")
async def verify_otp(verification_data: OTPVerification):
    user_manager.verify_otp(verification_data)
    return {"message": "Verification successful"}

@app.post("/enter-details/")
async def enter_details(user_details: UserDetails):
    user_manager.enter_details(user_details)
    return {"message": "Details saved successfully"}