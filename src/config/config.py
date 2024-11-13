import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = "newnvonubwnVNOASNVUBEDVNQAISNCVSswvwrebrewb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
