# **How To Run This App**

1. ## Install Dependencies
    - from the project root
        - ### If you use regular python:
        - in the terminal run: pip intall -r requirements.txt
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
        - ### Using VS code
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
         - in the aditional terminal window navigate to frontend folder using cd "input folder path"
            - example command: cd ".\generative_ai\text_summarizer_api\frontend" 
        - in the terminal run: npm run dev
        - **Or Using Python's built--in server:**
        - from the frontend folder using the same navigation trick as described above run
            - python -m http.server 5500
            - then look up: http://localhost:5500/index.html in web browser


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
1. ### **Short Text (< 1500 characters)*
Model: sshleifer/distilbart-cnn-12-6
- Very fast
- CPU‑friendly
- Great for short summaries
- Ideal for quick responses
2. ### **Medium Text (1500–5000 characters)*
Model: facebook/bart-large-cnn
- Higher‑quality summaries
- Better handling of moderately long text
- Still fully open‑source
3. ### **Long Text (5000+ characters)*
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
