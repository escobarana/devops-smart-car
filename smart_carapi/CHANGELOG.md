# Changelog 

## v1.0.0

- Create smart car REST API functionality using Flask fully tested
- Configuration of MongoDB Database
- Create Swaggger Documentation


## v1.0.1

- Add Dockerfile
- Add tests for Flask routes
- Configure CI with GitHub Actions Workflow


## v1.0.2

- Add docker-compose.yaml (Flask app + mongo + mongo express)
- Configure push Docker image to Docker Registry with GitHub Actions Workflow
- Add Kubernetes manifest files (Flask app + mongo)  --- k8s
- Configure deployment by adding Terraform configuration (using Terraform Cloud) --- IaC
- Configure CD (with terraform) with GitHub Actions Workflow


## v1.1.0

- Refactor `smart_carapi` directory
- Add monitoring with Prometheus and Grafana (personalised dashboard at `http://localhost:3000/d/smartcar` route)
- Update GitHub Actions workflows to match refactoring
