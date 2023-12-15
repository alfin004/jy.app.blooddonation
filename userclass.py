from sqlalchemy import create_engine, text
from pydantic import BaseModel
import random
import string
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

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

class UserManager:
    @staticmethod
    def create_user(user_create: UserCreate):
        # Generate OTP
        otp = "".join(random.choices(string.digits, k=6))

        # Save OTP to the database
        insert_query = text(
            "INSERT INTO users (mobile_number, username, otp) VALUES "
            "(:mobile_number, :username, :otp)"
        )
        with engine.connect() as connection:
            connection.execute(
                insert_query,
                {"mobile_number": user_create.mobile_number, "username": user_create.username, "otp": otp},
            )

        return otp

    @staticmethod
    def verify_otp(verification_data: OTPVerification):
        # Check OTP in the database
        update_query = text(
            "UPDATE users SET is_verified = 1, otp = NULL, password = :password "
            "WHERE otp = :otp"
        )
        with engine.connect() as connection:
            connection.execute(
                update_query,
                {"otp": verification_data.otp, "password": verification_data.password},
            )

    @staticmethod
    def enter_details(user_details: UserDetails):
        # Save user details
        update_query = text(
            "UPDATE users SET name = :name, address = :address, hometown = :hometown, "
            "blood_group = :blood_group WHERE username = :username AND is_verified = 1"
        )
        with engine.connect() as connection:
            connection.execute(
                update_query,
                {
                    "username": user_details.username,
                    "name": user_details.name,
                    "address": user_details.address,
                    "hometown": user_details.hometown,
                    "blood_group": user_details.blood_group,
                },
            )

# Your FastAPI application code without the dependency for the database session
