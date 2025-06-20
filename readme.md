# JWT Encoder/Decoder in Python

This project is a simple Python application that demonstrates how to create and decode JSON Web Tokens (JWT). It uses the popular `PyJWT` library to handle the encoding and decoding processes securely. The project is useful for understanding token-based authentication and how JWTs can be used to securely transmit information between parties.

## Features

- Encode data into a JWT using a secret key
- Decode and verify JWTs
- Handles expiration and payload claims
- Clean, minimal example ideal for learning or integrating into larger applications

## Technologies Used

- Python 3
- [PyJWT](https://pyjwt.readthedocs.io/)

## Usage

Generate a token:

```python
import jwt
token = jwt.encode({"user_id": 123}, "secret", algorithm="HS256")
```
