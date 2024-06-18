import os

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    MONGODB_URI = os.getenv("MONGODB_URI")
    MONGODB_NAME = os.getenv("MONGODB_NAME")
