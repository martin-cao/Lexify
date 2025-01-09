import requests

from controller.config_controller import load_config

def register(username: str, password: str):
    conf = load_config()
    url = f"{conf['SERVER_URL']}/register"
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
    conf = load_config()
    url = f"{conf['SERVER_URL']}/login"
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
    conf = load_config()
    url = f"{conf['SERVER_URL']}/edit"
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
