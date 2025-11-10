from flask import Flask, jsonify, Response
from services.berries_service import get_all_berry_stats
import logging
from flask_caching import Cache

logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")

app = Flask(__name__)
app.config.from_mapping({
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 3600
    })
cache = Cache(app)

@app.route("/allBerryStats", methods=["GET"])
@cache.cached()
def all_berry_stats()->Response:
    """Endpoint to get statistics for all  berries"""
    data = get_all_berry_stats()
    response = jsonify(data)
    # Ensure content-type header is explicitly set
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
