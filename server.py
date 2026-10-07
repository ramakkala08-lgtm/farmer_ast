from flask import Flask, jsonify, send_from_directory
from rainfall_baba import generate_weather_response
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")


@app.route("/")
def home():
    return send_from_directory(
        FRONTEND_DIR,
        "index.html"
    )


@app.route("/weather")
def weather():

    latitude = 17.9784
    longitude = 79.5941

    result = generate_weather_response(
        latitude,
        longitude
    )

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)