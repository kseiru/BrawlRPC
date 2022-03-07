from pypresence import Presence
from config import API_KEY, BRAWL_TAG, client_id
import json
from urllib.parse import quote
import requests
import time
from datetime import datetime

while True:
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
    brawlers = data["brawlers"]
    icon = data["icon"]["id"]

    def sort_trophies(x):
        return x["trophies"]

    brawlers.sort(key=sort_trophies, reverse=True)
    top_brawler = brawlers[0]

    top_brawler_name = top_brawler["name"]
    top_brawler_trophies = top_brawler["trophies"]
    try:
        RPC = Presence(client_id)
        RPC.connect()
        RPC.update(large_image=f"https://kseiru.ru/brawl/{icon}.png", details=f"{username} - {trophies} 🏆", state=f"Top brawler: {top_brawler_name} - {top_brawler_trophies} 🏆", large_text="Brawl Stars", start=int(datetime.now().timestamp()))
    except:
        print("Something went wrong...")
        exit()
    time.sleep(25)
print("RPC is Loaded!")

while True:
    time.sleep(15)