# service/tests/test_hash_endpoint.py
import re
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from service.main import app, resolve_cli_path  # resolve_cli_path is defined in main.py

# Skip test cleanly if the CLI binary isn't present yet
try:
    _cli_path = resolve_cli_path()
    _cli_exists = Path(_cli_path).is_file()
except Exception:
    _cli_exists = False

pytestmark = pytest.mark.skipif(not _cli_exists, reason="cli_app missing; build it first (cmake & ninja)")


# Regex for a 64-char lower/uppercase hexadecimal string
SHA256_PATTERN = re.compile(r"^[a-f0-9]{64}$")

def test_hash_endpoint_returns_sha256():
    # Use context manager so FastAPI lifespan (startup) runs and sets app.state.cli_path
    with TestClient(app) as client:
        resp = client.get("/hash", params={"msg": "abc"})
        assert resp.status_code == 200, resp.text
        data = resp.json()
        assert "hash" in data, "Response must include 'hash'"
        assert SHA256_PATTERN.fullmatch(data["hash"]), f"Not a valid SHA-256: {data['hash']}"