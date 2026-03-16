"""
AI Prediction API for Smart Environmental Station.
Serves /predict for rain probability and irrigation advice.
No API keys required — runs locally for expo/demo.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)


def predict_rain_and_irrigation(temperature, humidity, pressure, uv_index, aqi):
    """
    Simple rule-based prediction (no external API or trained model needed).
    For expo/demo. Replace with a real model (e.g. joblib.load("weather_model.pkl"))
    if you have historical data.
    """
    # Heuristic: high humidity + low pressure often means rain likely
    rain_score = 0.0
    rain_score += (humidity / 100) * 0.4
    if pressure < 1010:
        rain_score += 0.3
    elif pressure < 1000:
        rain_score += 0.5
    if humidity > 70 and pressure < 1015:
        rain_score += 0.2
    rain_score = min(1.0, rain_score)

    rain_prediction = rain_score >= 0.5
    rain_probability_percent = round(rain_score * 100, 1)

    # Irrigate only if rain is unlikely (so we don't waste water)
    irrigation_needed = rain_probability_percent < 30

    if rain_probability_percent > 70:
        alert = "Heavy rain expected"
    elif rain_probability_percent > 50:
        alert = "Rain likely"
    elif rain_probability_percent > 30:
        alert = "Possible rain"
    else:
        alert = "Clear"

    return {
        "rain_prediction": rain_prediction,
        "rain_probability_percent": rain_probability_percent,
        "irrigation_needed": irrigation_needed,
        "alert": alert,
    }


@app.route("/")
def index():
    """Root route: return same prediction as /predict so localhost:5000 gives responses."""
    return predict()


@app.route("/predict", methods=["GET", "POST"])
def predict():
    """
    GET: use default demo values.
    POST or GET with query params: temperature, humidity, pressure, uv_index, aqi
    (for future use when Next.js sends live sensor values).
    """
    if request.method == "POST":
        body = request.get_json(silent=True) or {}
        temperature = float(body.get("temperature", 28.4))
        humidity = float(body.get("humidity", 54))
        pressure = float(body.get("pressure", 1012))
        uv_index = float(body.get("uv_index", 3.2))
        aqi = float(body.get("aqi", 87))
    else:
        temperature = float(request.args.get("temperature", 28.4))
        humidity = float(request.args.get("humidity", 54))
        pressure = float(request.args.get("pressure", 1012))
        uv_index = float(request.args.get("uv_index", 3.2))
        aqi = float(request.args.get("aqi", 87))

    result = predict_rain_and_irrigation(
        temperature, humidity, pressure, uv_index, aqi
    )
    return jsonify(result)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "ai-predictor"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
