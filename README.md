# PokeAPI Berries Statictics API

A Python + Flask API that consumes the PokeAPI to retrieve berry data and compute growth-time statistics.

This project’s goal is to:
- Consume data from PokeAPI
- Compute key statistics such as min, max, mean, median, variance, and frequency for each berry’s growth_time
- Return the data in JSON format
- Display an interactive histogram
- Run in a containerized production environment

Flow summary:
The API fetches berry data from PokeAPI.
Extracts and processes growth_time values.
Caches results for 1 hour via Flask-Caching.
Optionally generates a histogram to visualize the distribution.


## Live Deployment

Production URL: https://favourite-helene-asda-02cab572.koyeb.app/

### Available Endpoints
Endpoint :[/allBerryStats](https://favourite-helene-asda-02cab572.koyeb.app/allBerryStats)
- method : GET
- desc : Returns computed berry growth time statistics

Endpoint : [/berryHistogram](https://favourite-helene-asda-02cab572.koyeb.app/berryHistogram)
- method : GET
- desc : Displays histogram visualization


endpoint : [/health](https://favourite-helene-asda-02cab572.koyeb.app/health)
- method : GET or HEAD
- desc : Basic API health check

Details
- Hosted on Koyeb
- Status: Healthy
- Port: 8000 (aligned with Koyeb default)
- Server: Gunicorn
- Auto-deploys from GitHub main branch
- Health monitored automatically by Koyeb

## Local Setup
Clone the repo
``` python
git clone https://github.com/iangenta/pokeberries
cd pokeberries

```

create and activate virtual env
``` python
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

install dependencies

``` python
pip install -r requirements.txt
```

## Environment variables
create a .env file in the project root

- POKEAPI_BASE_URL=https://example.com/
- CACHE_TIMEOUT=3600
- FLASK_ENV=production

## Run with docker

Build and start

``` bash
docker-compose up --build
```

health check
``` bash
curl http://127.0.0.1:5000/health
```
expected response
``` json
{"status": "ok"}
```


## API ENDPOINTS

endpoint : /allBerryStats 
- method : GET
- desc : Returns computed berry growth time statistics
- Example JSON Response:
``` json
{
  "berries_names": ["cheri", "chesto", "pecha", "..."],
  "min_growth_time": 2,
  "max_growth_time": 24,
  "median_growth_time": 15.0,
  "mean_growth_time": 12.86,
  "variance_growth_time": 62.47,
  "frequency_growth_time": {
    "2": 5,
    "3": 5,
    "4": 3
  }
}
```


endpoint : /berryHistogram 
- method : GET
- desc : Displays histogram visualization

endpoint : /health 
- method : GET or HEAD
- desc : Basic API health check

## Testing
Run tests using 
``` bash
pytest -v
```

Tests cover:
 - compute_stats() calculations
 - Mocked PokeAPI responses via requests-mock




