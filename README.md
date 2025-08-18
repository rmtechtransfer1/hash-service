# Example Repo

## Objective:

A mini DevSecOps project, demonstrating end-to-end pipeline with components necessary for a cATO. 

## Contents

- C++ command-line utility [(cpp)]()
- A FastAPI microservice that wraps that utility behind an HTTP endpoint. [(service)]()
- Github workflows and actions containing the mini cATO [(pipeline)]()

## Workflows

- [Software Factory]()
Purpose: The software-factory pipeline is a comprehensive CI/CD workflow that builds, tests, scans, signs, and releases a containerized C++/Python application with full supply chain security artifacts including SBOMs, SLSA provenance, and vulnerability reports.

- [Policy-check]()
Purpose: The policy pipeline validates infrastructure-as-code and Kubernetes manifests against security compliance rules using Open Policy Agent (OPA/Rego), enforcing best practices for container security, and resource configurations before deployment. (Note- runs only on select folders)

## Documents provided

- ## [10 Minute Quick Start- Start Here!]() 
- [Supply Chain mapping]()
- [Zero-to-Prod]()

## Quick Top-Level TOC

- [.github]() - Workflows for pipeline
- [cpp]() - C++ app
- [Docker]() - Primary Dockerfile used in the app
- [Documentation]() - Relates to Quickstart, Release, SupplyChainMapping, and other related commands
- [kubernetes]() - K8s yaml files used in the app
- [Scripts]() - Reusable scripts used for GH Workflows and Actions
- [security_compliance]() - Related configuration files used for GH Workflows and Actions
- [Service]() - webapi (Python/FastAPI)
- [thirdparty]() - Related 3rd party libraries 

