# IntelliTicket: AI-Powered Support Ticket Creation

IntelliTicket is a system that uses generative AI to analyze customer support emails and automatically create support tickets with summarized information, priority, and category.

## Features

- FastAPI backend for ticket creation
- Streamlit frontend for user interaction
- Gemini AI model for email analysis
- Dockerized for easy deployment

## Project Structure

```
.env
.gitignore
docker-compose.yml
Dockerfile.fastapi
Dockerfile.streamlit
requirements.txt
src/
    agent.py
    main.py
    streamlit_app.py
    test_agent.py
```

## Getting Started

### Prerequisites

- Docker
- Python 3.11 (for local development)
- Gemini API Key (set in `.env` as `GEMINI_API_KEY`)

### Running with Docker

1. Build and start the services:
    ```sh
    docker-compose up --build
    ```
2. Access the Streamlit app at [http://localhost:8501](http://localhost:8501).

### Running Locally

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Set your Gemini API key in `.env`:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```
3. Start FastAPI backend:
    ```sh
    uvicorn src.main:app --host 0.0.0.0 --port 8080
    ```
4. Start Streamlit frontend:
    ```sh
    streamlit run src/streamlit_app.py
    ```

## Usage

- Paste a support email in the Streamlit app.
- Click "Analyze & Create Ticket".
- View the generated summary, priority, and category.

## Testing

Run the agent test script:
```sh
python src/test_agent.py
```

