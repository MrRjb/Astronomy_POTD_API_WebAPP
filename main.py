import streamlit
import requests

API_KEY = "zqW6hLvEszHaJaZODCKSYcUx9upzHamshYxgIHhm"

URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(URL)
content = response.json()

# streamlit.set_page_config(layout="wide")

streamlit.title(content['title'])

img_url = content['url']

response = requests.get(img_url)
image = response.content

with open("image.jpg", "wb") as file:
    file.write(image)
    
streamlit.image("image.jpg")

streamlit.write(content['explanation'])