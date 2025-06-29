# 🚀 Python Flask App + Prometheus + Grafana (Mini Monitoring Project)

This is a **mini hands-on project** to learn:
- Docker & Docker Compose
- Building a Python Flask app exposing Prometheus metrics
- Setting up Prometheus to scrape those metrics
- Visualizing in Grafana dashboards

> ✅ Great for DevOps, SRE, or observability practice.

---

## ✨ **Project Architecture**

```mermaid
graph TD
    A[Flask App] -- Exposes /metrics --> B[Prometheus]
    B -- Data Source --> C[Grafana]
    C -- Visualizes --> D[Dashboards]


🛠 Tech stack
Python 3 + Flask

prometheus_client library

Prometheus

Grafana⚙️ Setup instructions
Requires: Docker & Docker Compose installed

1️⃣ Clone the repo
bash
Copy
Edit
git clone git@github.com:yourusername/yourrepo.git
cd yourrepo
2️⃣ Build and run with Docker Compose
bash
Copy
Edit
docker compose up --build
(Add -d to run in background)

3️⃣ Access services
Service	URL	Default login
Flask App	http://localhost:5000/	—
Prometheus	http://localhost:9090	—
Grafana	http://localhost:3000	admin / admin

Replace localhost with your EC2/VPS public IP if running remotely.

📊 Grafana setup
Login to Grafana

Go to ⚙️ Configuration → Data Sources → Add data source

Select Prometheus

URL: http://prometheus:9090

Click Save & Test

🔍 Prometheus metrics
The Flask app exposes:

app_request_latency_seconds_count: total request count

app_request_latency_seconds_sum: total request latency

Histogram buckets: request latency distribution

✅ Build your dashboard
In Grafana, create new panels with:

Total requests:

promql
Copy
Edit
app_request_latency_seconds_count
Average latency over last minute:

promql
Copy
Edit
rate(app_request_latency_seconds_sum[1m]) / rate(app_request_latency_seconds_count[1m])
Requests per second:

promql
Copy
Edit
rate(app_request_latency_seconds_count[1m])
🐍 Python app overview
Exposes metrics at /metrics

Example app responds at /

See app/app.py.

**🐳 Project structure**
Copy
Edit
.
├── docker-compose.yml
├── prometheus
│   └── prometheus.yml
├── grafana
├── app
│   ├── app.py
│   ├── requirements.txt
└── README.md
✏️ Customize
Add more endpoints in Flask

Create Grafana alerts

Add exporters or scrape other services

❤️ Credits & License
Open-source for learning. Feel free to fork, modify, and share!
MIT License.



Docker & Docker Compose



