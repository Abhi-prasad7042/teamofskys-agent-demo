import jwt

def login_user(username, password):
    if username == "admin" and password == "1234":
        token = jwt.encode({"user": username}, "secret_key", algorithm="HS256")
        return token
    return None

def verify_token(token):
    try:
        return jwt.decode(token, "secret_key", algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None