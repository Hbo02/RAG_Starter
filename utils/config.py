## utils/config.py
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

def get_env_var(key):
    return os.getenv(key)
