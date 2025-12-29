import subprocess, time, os, pytest, logging, sys, socket

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
def wait_for_port(host, port, timeout=10):
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except OSError:
            time.sleep(0.5)
    raise RuntimeError(f"Server {host}:{port} did not start in time")


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
    wait_for_port("127.0.0.1", 5500) # Wait for server to start
    yield
    logging.info("Stopping frontend server after tests")
    process.terminate()