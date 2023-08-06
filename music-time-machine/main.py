from bs4 import BeautifulSoup
import requests


date_back_to = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
URL = f"https://www.billboard.com/charts/hot-100/{date_back_to}"
content = requests.get(URL)
soup = BeautifulSoup(content.text, "html.parser")
song_name_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_name_spans]

