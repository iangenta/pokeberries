# app.py
from flask import Flask, jsonify, Response
from services.berries_services import get_all_berry_stats
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")

app = Flask(__name__)

@app.route("/allBerryStats", methods=["GET"])
def all_berry_stats()->Response:
    """Endpoint to get statistics for all  berries"""
    data = get_all_berry_stats()
    response = jsonify(data)
    response.headers["Content-Type"] ="application/json"
    return response

if __name__ == "__main__":
    app.run(debug=True)
