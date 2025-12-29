import subprocess, time, os, pytest, logging, sys

# ---------- Logging: Minimal Setup ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test_container_1.log", mode="w"),
        logging.StreamHandler(sys.stdout)
    ],
    force=True
)

# ---------- Fixture: Start Frontend Server ----------
@pytest.fixture(scope="session", autouse=True)
def start_frontend_server():
    logging.info("Starting frontend server for tests")
    # Resolve frontend directory RELATIVE to project root
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    frontend_path = os.path.join(project_root, "frontend")
    logging.info(f"Serving frontend from: {frontend_path}")

    process = subprocess.Popen(
        ["python", "-m", "http.server", "5500", "--bind", "127.0.0.1"],
        cwd = frontend_path
    )
    time.sleep(3) # Wait for server to start
    yield
    logging.info("Stopping frontend server after tests")
    process.terminate()