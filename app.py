from flask import Flask, jsonify, Response, render_template
from services.berries_service import( get_all_berry_stats , gen_histogram)
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


@app.route("/berryHistogram",methods=["GET"])
def berry_histogram() -> Response:
    "Display histogram of berry growth times as HTML"
    stats = get_all_berry_stats()
    growth_times= []

    for time_str, freq in stats["frequency_growth_time"].items():
        growth_times.extend([int(time_str)]*freq)

    img_data = gen_histogram(growth_times)
    return render_template("histogram.html",img_data=img_data)


@app.route("/health",methods=["GET","HEAD"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
