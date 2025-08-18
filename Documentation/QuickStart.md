# 10 Minute Quick Start

## Requirements
 
```
Python 3.11.9 on Ubuntu 22.04
Docker installed and running
kind installed
```

## Clone Repo 
```
git clone {TBD}
```

## CMAKE - building

*** All following commands from repo root ***

Environment setup
```bash
sudo apt update
sudo apt install -y build-essential ninja-build cmake
```

Run cmake ci-local
```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --target cli_app -j
```

Verify binary created
```bash
ls -l ./build/bin/cli_app 

# Expected output: 
-rwxrwxr-x 1 user user 63080 {Build Time} ./build/bin/cli_app
```

Run CLI script
```bash
./build/bin/cli_app --message testing123

#Expected output: 
[INFO] [2025-08-09 23:49:13 UTC] b822f1cd2dcfc685b47e83e3980289fd5d8e3ff3a82def24d7d1d68bb272eb32
```
## Kubernetes Setup

If Kind cluster not already setup, or desire a new cluster for testing. If using an existing cluster, skip to next step (Kubernetes Deployment)

Create a kind cluster with custom configuration:

```bash
# Create a simple cluster
kind create cluster --name demo-cluster
```
Verify cluster is running:
```bash
kubectl cluster-info --context kind-demo-cluster
kubectl get clusters
# Expected output: 
demo-cluster
```
## Kubernetes Deployment
Export cluster name for use in all commands below
```bash
export CLUSTER_NAME=$(kind get clusters 2>/dev/null | head -n1)
```

Build your Docker image
```bash
# Build the Docker image
docker build -f Docker/Dockerfile -t hash-service:latest .

# Verify the image was created
docker images | grep hash-service

# Expected output: 
hash-service  latest
```
Load your Docker image into the kind cluster
```bash
# Load the image into the cluster (note- may take a minute to finish loading)
kind load docker-image hash-service:latest --name ${CLUSTER_NAME}

# Expected output:
Image: "hash-service:latest" with ID "sha256:{cooresponding SHA256}"
```

Apply the Kubernetes deployment manifest:

```bash
# Apply the deployment manifest
kubectl apply -f kubernetes/deployment.yml

# Wait for pods to come up
kubectl wait --for=condition=ready pod -l app=hash-service -n hash-service --timeout=60s

# Verify services running
kubectl get all -n hash-service

# Port forward
kubectl port-forward -n hash-service svc/hash-service 8080:8080 &
```
Visit on the browser
```bash

# Check healthz to verify everything working correctly
Visit Browser: http://127.0.0.1:8080/healthz

# Visit /hash
http://127.0.0.1:8080/hash?msg=testing123
```

Clean up
```bash
# Delete Cluster (***WARNING - this is optional - proceed with caution***)
kind delete cluster --name ${CLUSTER_NAME}
```
***Congrats! You are complete with the Demo***