import requests
import json
import os

from config import Config

def load_config():
    if not os.path.exists(Config.CONFIG_PATH):
        print("[WARNING] Config load error. No config.json found.")
        return
    with open(Config.CONFIG_PATH, 'r') as config_file:
        return json.load(config_file)

def save_config(config):
    if not os.path.exists(Config.CONFIG_PATH):
        print("[WARNING] Config load error. No config.json found.")
        return
    with open(Config.CONFIG_PATH, 'w') as config_file:
        json.dump(config, 'f', indent=4)

