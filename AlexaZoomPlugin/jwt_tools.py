import jwt
import os
from time import time
import json


def generate_jwt():
    CLIENT_KEY = os.environ.get("CLIENT_KEY")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    data = {
        "token": jwt.encode(
            {
                "aud": None,
                "iss": CLIENT_KEY,
                "exp": int(time())+ 90 * 86400,
                "iat": int(time())
            }, CLIENT_SECRET
        ).decode('utf-8')
    }
    return json.dumps(data)

if __name__ == "__main__":
    print(generate_jwt())