import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

print('in jwt generator')

load_dotenv()

# Define the payload (claims)
payload = {
    "user_id": "12345",
    "username": "example_user",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)  # Expiration time
}

# Define the secret key and algorithm
secret_key = os.getenv("SECRET_KEY")

print(secret_key)

algorithm = "HS256"  # HMAC SHA256

# Encode the JWT
encoded_jwt = jwt.encode(payload, secret_key, algorithm=algorithm)

print(f"Generated JWT: {encoded_jwt}")