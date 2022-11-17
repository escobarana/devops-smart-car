# Changelog 

## v1.0.0

- Create smart car REST API functionality using Flask fully tested
- Configuration of MongoDB Database
- Create Swaggger Documentation


## v1.0.1

- Add Dockerfile
- Add tests for Flask routes
- Configure CI with GitHub Actions Workflow


## v1.1.0

- Add docker-compose.yaml (Flask app + mongo + mongo express)
- Configure push Docker image to Docker Registry with GitHub Actions Workflow
- Add Kubernetes manifest files (Flask app + mongo)  --- k8s
- Configure deployment by adding Terraform configuration (using Terraform Cloud) --- IaC
- Configure CD (with terraform) with GitHub Actions Workflow


## v1.2.0

- Refactor `smart_carapi` directory
- Add monitoring with Prometheus and Grafana (personalised dashboard at `http://localhost:3000/d/smartcar` route)
- Update GitHub Actions workflows to match refactoring


## v1.3.0

- Add Canary Deployment using Istio for service mesh


## v1.3.1

- Add documentation for each part performed


## v1.3.2

- Update GitHub Actions workflows to make them dependent on each other (only possible in the main branch)
