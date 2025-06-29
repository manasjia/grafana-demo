from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest


import time
import random 

app = Flask(__name__)


REQUEST_COUNT = Counter('app_request_count', 'Total app HTTP request count', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency', ['endpoint'])

@app.route("/")
def index():
    start = time.time()
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    time.sleep(random.uniform(0.1, 0.5))  # simulate latency
    REQUEST_LATENCY.labels(endpoint='/').observe(time.time() - start)
    return "Hello, Prometheus!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
