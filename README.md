# GitHub Repo to Speech

This project fetches a GitHub repository's contents, stores them in a Weaviate vector database, and converts the text to speech.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your `config.py` file with your API keys
4. Run the main script: `python main.py`

## Configuration

Create a `config.py` file with the following content:

```python
GITHUB_TOKEN = 'your_github_token'
WEAVIATE_URL = 'http://localhost:8080'  # Replace with your Weaviate instance URL
GOOGLE_APPLICATION_CREDENTIALS = 'path/to/your/google_credentials.json'
```

Replace the placeholder values with your actual API keys and credentials.
