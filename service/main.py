# main.py : Defines the FASTAPI application for a simple hash service.
#
# Usage:
# Ex: http://127.0.0.1:8080/hash?msg=testin123
# Ex: curl --get --data-urlencode "msg=testing123" http://127.0.0.1:8080/hash
# 
# To-Dos:
# Additional HTTP behavior and validation error handling (i.e. msg empty or missing)
# Additional endpoingts (i.e. /readyz)

import os
import subprocess
import logging
from pathlib import Path
from typing import Annotated
from contextlib import asynccontextmanager

from fastapi import FastAPI, Query, HTTPException
from dotenv import load_dotenv

log = logging.getLogger("uvicorn.error")

# Paths & config
SERVICE_DIR = Path(__file__).resolve().parent
REPO_ROOT = SERVICE_DIR.parent    

# Load .env from service
load_dotenv(SERVICE_DIR / ".env")

# Read config
RAW_CLI = os.getenv("CLI_APP_PATH", "./build/bin/cli_app")

# Resolve CLI path
def resolve_cli_path() -> Path:
    cli = Path(RAW_CLI)
    if not cli.is_absolute():
        cli = (REPO_ROOT / cli).resolve()
    return cli

# Lifespan (startup)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app.state.cli_path = resolve_cli_path()
    if not app.state.cli_path.is_file():
        msg = f"CLI binary missing at {app.state.cli_path}. Build it or adjust CLI_APP_PATH in service/.env."
        log.error(msg)
        raise RuntimeError(msg)
    log.info("CLI_APP_PATH resolved to %s (exists=True)", app.state.cli_path)
    yield
    # Shutdown (nothing to clean up)
    return

app = FastAPI(title="Hash API", lifespan=lifespan)

# Health check endpoint
@app.get("/healthz")
def health():
    return {"status": "ok"}

# Hash endpoint
@app.get("/hash")
def hash_message(msg: Annotated[str | None, Query(min_length=1)]):
    cli = app.state.cli_path
    try:
        result = subprocess.run([cli, "--message", msg], capture_output=True, text=True, check=True)
        token = result.stdout.strip().split()[-1]
        if len(token) != 64 or any(c not in "0123456789abcdefABCDEF" for c in token):
            raise HTTPException(500, "malformed hash from cli")
        return {"hash": token.lower()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error running CLI: {e.stderr}")
    
# Runs FASTAPI app with Uvicorn server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080
    )
