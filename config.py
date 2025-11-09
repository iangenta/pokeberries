import os
from dotenv import load_dotenv

load_dotenv()
POKEAPI_BASE_URL = os.getenv("POKEAPI_BASE_URL")