
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/upload")
def get_data():
    url = "https://jsonplaceholder.typicode.com/"

    response =  requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")

    title = []

    for item in soup.find_all("a" , class_="story_link"):
        title.append(item.text)

        return{
            "news": title[:5]
        }

