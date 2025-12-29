# **How To Run This App**
    - This project is intentionally documented for beginners who are learning how to connect frontend, backend, and ML together
1. ## Install Dependencies
    - from the project root
        - ### If you use regular python:
        - in the terminal run: pip install -r requirements.txt
        - note: If you prefer installing dependencies from pyproject.toml run: pip install .
        - ### If you use uv:
        - in the terminal run: uv sync
2. ## Run the Backend Server
    - from the project root
        - ### Regular Python
        - in the terminal run: python main.py
        - ### Using uv
        - in the terminal run: uv run main.py
            - or uv run ./main.py
        - ### Using VS Code
        - open main.py
        - click the run button in the top-right corner
3. ## Run the Frontend
    - open frontend folder then click on index.html file to open it
        - ### Option A - Using VS Code Live Server (recommended)
        1. install the Live Server extension VS Code
        2. Click Go Live in the bottom-right corner
        3. Your browser will open the app automatically
    - open an additional terminal using the + button in the VS Code terminal
        - ### Option B - Without Live Server
        - If you don't want the extension, you can run a simple dev server:
         - **If you have Node.js installed:**
         - in the additional terminal window navigate to frontend folder using cd "input folder path"
            - example command: cd ".\generative_ai\text_summarizer_api\frontend" 
        - in the terminal run: npm run dev
        - **Or Using Python's built-in server:**
        - from the frontend folder using the same navigation trick as described above run
            - python -m http.server 5500
            - then look up: http://localhost:5500/index.html in web browser
4. ## Running Backend
    - Initial requests may fail while models load (~60s or longer depending on your machine). This is expected.
        - as long as uvicorn doesn't give you an error message which is displayed in the terminal, the servers are just getting started.
    - Refresh page when you get something like:
        - INFO:     127.0.0.1:61482 - "GET / HTTP/1.1" 200 OK

5. ## Running Tests
    - Before running tests make sure the backend is running using the instructions above
    - For the frontend navigate to the index.html folder using the above python instructions then run
        - python -m http.server 5500 --bind 127.0.0.1
    - ## **Note all servers should be runing before test starts**
    - ### **Run the Entire Test Suit**
        - from the project root run:
            - #### *Python only*
            - pytest -vv
            - ##### *Run Backend Tests only*
            - pytest tests/test_backend -vv
            - ##### *Run Frontend Tests only (Selenium)*
            - pytest tests/test_frontend -vv
            - #### *uv*
            - uv run pytest tests
            - ##### *Run Backend Tests only*
            - uv run pytest tests/test_backend
            - ##### *Run Frontend Tests only (Selenium)*
            - uv run pytest tests/test_frontend
    
    - ### **Notes & Troubleshooting**
        - #### *No Internet Required:*
            - The project uses the system-installed EdgeDriver instead of webdriver_manager, so tests run fully offline
        - #### *If the frontend test fails instantly:*
            - Ensure your folder structure matches the expected layout and that the frontend/ directory exists at the project root.
        - #### *If the backend appears “stuck” on startup:*
            - This is normal — large transformer models take time to load.


# **Feature: Smart Model Swapping**
- This project includes a **dynamic model‑selection system** that automatically chooses the most efficient summarization model based on the length of the input text. The goal is to balance **speed, quality, and resource usage** while staying entirely within the world of free, open‑source models.

## **Why Model Swapping Matters**
- Different transformer models have different strengths:
    - Some are fast but have short context limits
    - Some are high‑quality but slower
    - Some can handle very long documents but require more compute
- Instead of forcing one model to handle every scenario, this app intelligently selects the best model for the job. This mirrors how real production systems optimize performance without sacrificing output quality.

## **How It Works**
The backend checks the length of the input text and routes it to one of three summarization models:
1. ### *Short Text (< 1500 characters)*
Model: sshleifer/distilbart-cnn-12-6
- Very fast
- CPU‑friendly
- Great for short summaries
- Ideal for quick responses
2. ### *Medium Text (1500–5000 characters)*
Model: facebook/bart-large-cnn
- Higher‑quality summaries
- Better handling of moderately long text
- Still fully open‑source
3. ### *Long Text (5000+ characters)*
Model: allenai/led-base-16384
- Designed for long documents
- Supports up to 16,384 tokens
- Ideal for articles, essays, transcripts, and large inputs
## **Benefits of This Approach**
- **Efficiency:** Small inputs don’t waste time on large models
- **Quality:** Medium and long inputs get better summarization
- **Scalability:** The system can grow with additional models
- **Transparency:** Users know exactly why a model was chosen
- **Zero Cost:** All models are free and open‑source
This feature demonstrates practical engineering tradeoffs and shows how to build a flexible, scalable ML‑powered API without relying on paid services.
