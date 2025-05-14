# app/main.py
from flask import Flask, request, jsonify
import joblib
import time
import psutil
import numpy as np

app = Flask(__name__)

# Load the model once when the server starts
model = joblib.load("v1_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)

    start = time.time()
    prediction = model.predict(features)
    end = time.time()

    memory = psutil.Process().memory_info().rss / 1024**2  # in MB

    return jsonify({
        "prediction": prediction.tolist(),
        "inference_time": round(end - start, 4),
        "memory_usage_mb": round(memory, 2),
        "model_version": "v1"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
