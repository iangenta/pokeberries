import logging
import requests
import io
import base64
from typing import Dict, List, Any
from statistics import median, mean, variance
from collections import Counter
from config import POKEAPI_BASE_URL
import matplotlib.pyplot as plt


logger = logging.getLogger(__name__)

EMPTY_STATS = {
    "berries_names": [],
    "min_growth_time": 0,
    "median_growth_time": 0.0,
    "max_growth_time": 0,
    "variance_growth_time": 0.0,
    "mean_growth_time": 0.0,
    "frequency_growth_time": {}
}


def fetch_all_berries()->List[Dict[str, Any]]:
    """Fetch all berries from the PokeAPI"""
    url = f"{POKEAPI_BASE_URL}/berry/"
    all_berries = []
    # The API is paginated so we keep looping until next is None
    
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
    """Compute statistics from a list of growth times."""
    if not growth_times:
        return {
            'min_growth_time': 0,
            'max_growth_time': 0,
            'median_growth_time': 0.0,
            'mean_growth_time': 0.0,
            'variance_growth_time': 0.0,
            'frequency_growth_time': {}
        }

    min_val = min(growth_times)
    max_val = max(growth_times)
    mean_val = mean(growth_times)
    median_val = median(growth_times)

    if len(growth_times) < 2:
        # variance() raise Statics error with <2 items
        variance_val = 0.0
    else: 
        variance_val = variance(growth_times)

    frequency = dict(Counter(growth_times))

    return {
        'min_growth_time': min_val,
        'max_growth_time': max_val,
        'median_growth_time': median_val,
        'mean_growth_time': mean_val,
        'variance_growth_time': variance_val,
        'frequency_growth_time': frequency
    }

def get_all_berry_stats()->Dict[str, Any]:
    all_berries =fetch_all_berries()
    if not all_berries:
        return EMPTY_STATS

    berries_names = [berry["name"] for berry in all_berries]
    growth_times =[]

    for berry in all_berries:
        berry_detail = fetch_berry_detail(berry['url'])
        if berry_detail and 'growth_time' in berry_detail:
            growth_times.append(berry_detail['growth_time'])

    stats = compute_stats(growth_times)    

    return {
        "berries_names": berries_names,
        **stats
    } 


def gen_histogram(growth_times: List[int]):
    if not growth_times:
        return ""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(growth_times, bins=10, color="blue", edgecolor="black")
    ax.set_title("Berry Growth Time Distribution")
    ax.set_xlabel("Growth time")
    ax.set_ylabel("Freq")

    #save image to memory
    buff = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buff,format="png")
    plt.close(fig)
    buff.seek(0)

    # encode image to embed in html
    img_b64 = base64.b64encode(buff.read()).decode("utf-8")
    return f"data:image/png;base64,{img_b64}"