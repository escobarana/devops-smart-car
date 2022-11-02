# This configuration file will contain the provider configurations and tested versions.
# Specify the Terraform provider version.
# Configure the AWS Provider

# Configure the Docker & AWS Providers
terraform {
  required_providers {
    docker = {
      source    = "kreuzwerker/docker"
      version   = "~> 2.20.0"
    }
    aws = {
      source    = "hashicorp/aws"
      version   = "~> 4.16"
    }
  }

  cloud {
    organization = "escobarana"

    workspaces {
      name = "gh-actions-smartcar"
    }
  }
}

provider "docker" {}  # Pull the image from Docker Hub

provider "aws" {  # Configure AWS
  region = var.region
  access_key = var.access_key
  secret_key = var.secret_access_key
}
