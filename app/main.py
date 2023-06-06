from fastapi import FastAPI
import bcrypt

app = FastAPI()

@app.post("/register")
def register(password):
    encrypted_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return {"encrypted_password": encrypted_password}

@app.post("/login")
def login(password):
    if bcrypt.checkpw(password.encode('utf-8'), encrypted_password):
        return "Access granted"
    else:
        return "Access denied"