import json
import os

from config import Config

def load_config():
    """
    Load the configuration from the config.json file.
    If the file does not exist or is empty, return an empty dictionary.
    """
    if not os.path.exists(Config.CONFIG_PATH):
        print("[WARNING] Config load error. No config.json found.")
        return {}
    try:
        with open(Config.CONFIG_PATH, 'r') as config_file:
            content = config_file.read()
            if not content.strip():
                print("[WARNING] Config file is empty. Returning default config.")
                return {}
            return json.loads(content)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to decode config.json: {e}")
        return {}
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred while loading config: {e}")
        return {}

def save_config(config):
    """
    Save the given configuration to the config.json file.
    If the directory does not exist, attempt to create it.
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(Config.CONFIG_PATH), exist_ok=True)
        with open(Config.CONFIG_PATH, 'w') as config_file:
            json.dump(config, config_file, indent=4)
            print("[INFO] Configuration saved successfully.")
    except Exception as e:
        print(f"[ERROR] An error occurred while saving config: {e}")