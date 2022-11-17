# Implement Monitoring to the containerized application

As seen in the main README.md file at the root of this project `devops-smart-car`, monitoring was implemented in 
`docker-compose.yml` file to monitor the containerized application.

In this folder you can find the configuration files for Prometheus under `prometheus` folder and for Grafana under `granafa`
folder. For grafana, a custom and personalized dashboard was built and configured linking prometheus to it.

![Grafana personalised dashboard port 3000](../image/dockercompose_monitoring/grafana-dashboards.png "Grafana Dashboard")

![Grafana monitoring dashboard port 3000](../image/dockercompose_monitoring/monitoring-grafana.png "Grafana Monitoring")
