# Topic: Monitoring ML model
 
This repository provide example of monitorign of an ML model for classification of red wine. 

## Task
	Monitoring of ML model using Prometheus and Grafana.

## Steps

1. Creating ML model of red wine classification based on redwine dataset (winequality-red.csv). 
- model is in the file SVM_red_wine.py
- model is saved as pickle file Rwinemodel.pkl
- metrics are saved into Prometheuis histogram (histogram.prom) using ModelMonitoringService from boxkite.monitoring.service

2. Model's metrics scrapping with Prometheus. 
- starting a simpe flask server on localhost:5000 with monitoring of model metrics (serve.py).
- sending request to the local server with data with changed features 

3. Connecting of Prometheus to Grafana.
- updating prometheus.yml file

```
- job_name: "features"
static_configs:
      - targets: ["localhost:5000"]%
```
- creating PromoQL query to make Kolmogorov-Smirnov test.

4. Getting a new dashbord in Grafana.
- the result is in the file "Red wine dashboard.png"

The work was done based on the ['video'](https://www.youtube.com/watch?v=07WQL8SJQwg)
	