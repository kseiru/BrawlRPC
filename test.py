import requests
from config import API_KEY, BRAWL_TAG
from urllib.parse import quote
import json

if "#" not in BRAWL_TAG:
    tag = f"#{BRAWL_TAG}"
else:
    tag = BRAWL_TAG

tag = quote(tag)


headers = {
    "Authorization": f"Bearer {API_KEY}"
}

get_player_data = requests.get(url=f"https://api.brawlstars.com/v1/players/{tag}", headers=headers)
data = get_player_data.content

data = json.loads(data)

username = data["name"]
trophies = data["trophies"]

icon = data["icon"]["id"]
print(icon)

print(username)
print(trophies)

brawlers = data["brawlers"]

def sort_trophies(x):
    return x["trophies"]

brawlers.sort(key=sort_trophies, reverse=True)
top_brawler = brawlers[0]

top_brawler_name = top_brawler["name"]
top_brawler_trophies = top_brawler["trophies"]
print(f"Top brawler: {top_brawler_name} - {top_brawler_trophies}")