







## Supplemental Documentation
### Docker

```bash
docker build -f Docker/Dockerfile -t hash-service .
docker run -d --name hash-api -p 8080:8080 hash-service
curl http://localhost:8080/healthz
curl "http://localhost:8080/hash?msg=testing123"
```

### Starting API

Environment setup 
```bash
sudo apt update
sudo apt install python3-venv
``` 

Create and activate Python virtual environment and env
```bash
source service/.venv/bin/activate
pip install -r service/requirements.txt
cp .env.example .env
```

Run python script
```
python3 service/main.py
```

Visit Health check endpoint to verify service up
```
http://127.0.0.1:8080/healthz
```

Visit Hash endpoint
```
http://127.0.0.1:8080/hash?msg=testing123
```

Exit virtual environment
```bash
deactivate
```

## Testing
### CMAKE Unit Tests
1. Follow CMAKE steps above to clone repo and run CMAKE
2. Run ctest ci-local
```ctest --test-dir build -C Debug --output-on-failure```
3. Expected output
```Unit tests - to be added```
### FastAPI
4.  Activate environment
```source service/.venv/bin/activate```
5. pytest service/test/test_hash_endpoint.py

