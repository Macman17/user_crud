from xml.etree.ElementTree import VERSION
from flask import (
    Flask, 
    request
)
from datetime import datetime
from app.database import user
import os.path

VERSION = "1.0.0"

app = Flask(__name__)

@app.get('/ping')
def ping():
    out={
        "status": "ok",
        "message": "pong"

    }
    return out

@app.get('/version')
def version():
    out={
        "status": "ok",
        "version": VERSION,
        "server_time": datetime.now().strftime("%F %H:%M:%S")

    }    
    return out

@app.get("/users")
def get_all_user():
    user_list = user.scan()
    out = {
        "status": "ok",
        "users": user_list
    }
    return out

@app.get("/users/<int:pk>")
def get_users_by_id(pk):
    record = user.select_by_id(pk)
    out = {
        "status": "ok",
    
    }
    if not record:
        out["status"] = "error"
        out["message"] = "not found"
        return out, 404
    else:
        out["user"] = record    
    return out

@app.post("/users")
def create_users():
    user_data = request.json
    user.insert(user_data)
    return "", 204

@app.put("/users/<int:pk>")
def update_users(pk):
    user_data = request.json
    user.update(pk, user_data)
    return "", 204

@app.delete("/users/<int:pk>")
def delete_user(pk):
    user.deactivate_user(pk)
    
    return "", 204
