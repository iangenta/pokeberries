import logging
import requests
from typing import Dict, List, Any
from statistics import median, mean, variance

from config import POKEAPI_BASE_URL
logger = logging.getLogger(__name__)

def fetch_all_berries()->List[Dict[str, Any]]:
    """Fetch all berries from the PokeAPI"""
    url = f"{POKEAPI_BASE_URL}/berry/"
    all_berries = []

    try:    
        while url:
            response = requests.get(url,timeout=10)
            response.raise_for_status()
            data = response.json()
            all_berries.extend(data['results'])
            url = data['next']
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching berries: {e}")
        return []

    return all_berries

def fetch_berry_detail(berry_url:str)->Dict[str, Any]:
    """Fetch a berry detail from the PokeAPI"""
    try:
        response = requests.get(berry_url,timeout=10)
        response.raise_for_status()
        berry_data = response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching berry detail: {e}")
        return {}

    return berry_data
    

def compute_stats(growth_times:List[int])->Dict[str, Any]:
    pass

def get_all_berry_stats()->Dict[str, Any]:
    pass 


