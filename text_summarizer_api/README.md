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
            - example command: cd "./generative_ai/text_summarizer_api/frontend" 
        - in the terminal run: npm run dev
        - **Or Using Python's built--in server:**
        - from the frontend folder using the same navigation trick as described above run
            - python -m http.server 5500
            - then look up: http://localhost:5500/index.html in web browser