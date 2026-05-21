from datetime import datetime
import jwt

SECRET = "super-secret-key"


def generate_token(username):
    payload = {
        "username": username,
        "exp": datetime.utcnow().timestamp() + 3600
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")


def verify_token(token):
    payload = jwt.decode(token, SECRET, algorithms=["HS256"])

    # ❌ BUG: incorrect datetime conversion
    expiration = datetime.fromtimestamp(payload["exp"])

    if expiration < datetime.utcnow():
        raise Exception("Token expired")

    return payload