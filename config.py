import os
from dotenv import load_dotenv

load_dotenv()

POKEAPI_BASE_URL = os.getenv("POKEAPI_BASE_URL")

if not POKEAPI_BASE_URL:
    raise EnvironmentError("Missing required enviroment variable : POKEAPI_BASE_URL")
 