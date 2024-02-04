# Example on how to use Prometheus and Grafana to monitor a Flask API Machine Learning Model application 

Example deployment of a Machine Learning Model Flask API with Gunicorn(WSGI) using Prometheus and Grafana for metrics and model monitoring. All tied together using docker-compose.

## Requirements
- docker compose

## Set up and run everything using docker-compose

```
docker compose up
```

## Access
* API: http://localhost:5000/
* Prometheus: http://localhost:9090/
* Grafana: http://localhost:3000 `[username: admin, password: admin]`


## Reference
https://github.com/jonashaag/prometheus-multiprocessing-example