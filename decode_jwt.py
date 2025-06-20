import jwt
from dotenv import load_dotenv
import os

load_dotenv()

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTIzNDUiLCJ1c2VybmFtZSI6ImV4YW1wbGVfdXNlciIsImV4cCI6MTc1MDQzNDU5M30.ZyKnh6xMl4qy_wCl3S0JE6dXqDMOTVOOVdG58ripIz0"  # Replace with your actual JWT token
secret_key = os.getenv("SECRET_KEY")
algorithm = "HS256"  # Replace with the algorithm used (e.g., "HS256", "RS256")

try:
    decoded_payload = jwt.decode(token, secret_key, algorithms=[algorithm])
    print("Decoded Payload:", decoded_payload)
except jwt.ExpiredSignatureError:
    print("Token has expired.")
except jwt.InvalidTokenError:
    print("Invalid token.")