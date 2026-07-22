# FastAPI Mock Web Scraper

A lightweight web crawling API built with **FastAPI**, **Requests**, and **BeautifulSoup4**. It scrapes the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) landing page to extract mock story or resource titles dynamically.

## 🚀 Features
* **FastAPI Backend**: High-performance, production-ready asynchronous framework.
* **HTML Parsing**: Robust extraction using BeautifulSoup4.
* **Automatic Docs**: Out-of-the-box interactive API documentation via Swagger UI.

## 🛠️ Prerequisites
Make sure you have Python 3.8+ installed on your machine.

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPO_NAME
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install fastapi uvicorn requests beautifulsoup4
   ```

## 💻 Code Overview
The main logic is located in `main.py`:

```python
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/upload")
def get_data():
    url = "https://jsonplaceholder.typicode.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = []

    for item in soup.find_all("a", class_="story_link"):
        title.append(item.text)
        
    # Fixed: Return statement moved outside the loop to fetch all 5 items
    return {
        "news": title[:5]
    }
```

## 🏃 Running the Application

Start the local development server using **Uvicorn**:
```bash
uvicorn main:app --reload
```
The server will start spinning at `http://127.0.0.1:8000`.

## 🗺️ API Endpoints & Testing

* **Scraper Route**: Send a `GET` request to `http://127.0.0` to fetch the parsed data.
* **Interactive API Documentation**: Visit `http://127.0.0` to view and test your endpoints interactively through Swagger UI.

## 📜 License
This project is open-source and available under the [MIT License](https://opensource.org).
