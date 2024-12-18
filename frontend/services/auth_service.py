import requests

from config import Config

def register(username: str, password: str):
    url = f"{Config.SERVER_URL}/register"
    payload = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status() # if HTTP code is not 2xx, then raise an error
        return response.json() # return JSON from backend
    except requests.RequestException as e:
        return {"success": False, "message": str(e)}

def login(username: str, password: str):
    url = f"{Config.SERVER_URL}/login"
    payload = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"success": False, "message": str(e)}

def logout(username):
    return {"success": True, "message": ""}

def edit_user(username, old_password, new_password: str):
    url = f"{Config.SERVER_URL}/edit"
    payload = {
        "username": username,
        "password": old_password,
        "new_password": new_password
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"success": False, "message": str(e)}
