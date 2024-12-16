# import requests
import json
import os

from config import Config
from controller.config_controller import load_config, save_config


def login(username, password):
    """
    Handle the login process. Write data into config.json
    :param username:
    :param password:
    :return:
    """

    payload = {
        'username': username,
        'password': password
    }

    # success, msg = AuthService.login(username, password)
    msg = ''
    if True: # if success
        config = load_config()
        config['username'] = username
        config['password'] = password
        save_config(config)
        return True, "登陆成功"
    else:
        return False, msg

def signup(username, password):
    """
    Handle the sign-up process. UI should auto login after sign up succeed. Write data into config.json
    :param username:
    :param password:
    :return:
    """

    # success, msg = AuthService.login(username, password)
    msg = ''
    if True:
        config = load_config()
        config['username'] = username
        config['password'] = password
        save_config(config)
        return True, "注册成功，自动登录"
    else:
        return False, msg

def logout():
    """
    Handle the log-out process.
    :return:
    """

    try:
        config = load_config()
        config.pop('username', None)
        config.pop('password', None)
        save_config(config)
        return True, "已登出"
    except Exception as exception:
        return False, f"登出失败，错误：{exception}"

