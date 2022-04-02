from boxkite.monitoring.service import ModelMonitoringService
from flask import Flask, request
import joblib
from boxkite.monitoring.collector import BaselineMetricCollector

model = joblib.load('Rwine_model.pkl')
    
app = Flask(__name__)
monitor = ModelMonitoringService(baseline_collector=BaselineMetricCollector(path="./histogram.prom"))


@app.route("/", methods=["POST"])
def predict():
    # User code to load features
    
    features = request.json
    score = model.predict_proba([features])[:, 0].item()

    pid = monitor.log_prediction(
        request_body=request.data,
        features=features,
        output=score,
    )

    res = {"Score": score, "prediction_id": pid}
    return res

@app.route("/metrics", methods=["GET"])
def metrics():
    return monitor.export_http()[0]

if __name__=="__main__":
    app.run()