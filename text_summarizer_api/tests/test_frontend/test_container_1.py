import pytest
import logging
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import subprocess, time, os

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

# ---------- Fixture: Browser Setup ----------
@pytest.fixture(scope="module")
def driver():
    option = Options()
    option.add_argument("--headless")
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=option)
    yield driver
    driver.quit()

# ---------- Test: Navigate to Page ----------
@pytest.mark.dependency(name="test_navigate_to_container_1_page")
def test_navigate_to_container_1_page(driver):
    logging.info("Starting test: Navigate to Container 1 page")
    #Navigate to the container 1 page and check if it loads correctly
    driver.get("http://127.0.0.1:5500/index.html")
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME,"container-1"))
        )
        assert True
        logging.info("Container 1 only page loaded Successfully")
    except Exception as e:
        logging.error(f"Error loading Container 1 only page: {e}, see screenshot: container_1_page_loaded_error.png")
        driver.save_screenshot("container_1_page_loaded_error.png")
        assert False

# ---------- Test: Send Input and Verify Output ----------
@pytest.mark.dependency(name="test_input_and_verify_output", depends=["test_navigate_to_container_1_page"])
def test_input_and_verify_output(driver):
    logging.info("Starting test: Input text and verify output")
    input_text = driver.find_element(By.ID, "container-1-text-input")
    summarize_button = driver.find_element(By.ID, "summarize-button")
    output_text = driver.find_element(By.ID, "container-1-summary-output")

    # Locate input field, send text, and click summarize button
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "container-1-text-input"))
        )
        input_text.clear()
        input_text.send_keys("Artificial Intelligence is transforming the world.")
        summarize_button.click()
        WebDriverWait(driver, 10).until(
            lambda d: output_text.text.strip() != ""
        )
        assert output_text.text != ""
        logging.info(f"Output generated successfully: {output_text.text}")
    except Exception as e:
        logging.error(f"Error verifying output: {e}, see screenshot: input_output_error.png")
        driver.save_screenshot("input_output_error.png")
        assert False
