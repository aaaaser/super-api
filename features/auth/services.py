def authenticate_credentials(username, password):
    if username == "user_demo" and password == "password123":
        return {"status": "success", "user_id": 101, "role": "admin"}
    return {"status": "failed", "message": "Invalid username or password"}