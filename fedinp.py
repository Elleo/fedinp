#!/usr/bin/env python3
from display import Display
from bs4 import BeautifulSoup
import requests
import time
import re

NP_URL = "https://radiofreefedi.net/np.php"

class NP:

    def __init__(self):
        self.d = Display()

    def run(self):
        while True:
            soup = BeautifulSoup(requests.get(NP_URL).text, features="html.parser")
            tds = soup.find_all("td")
            np = tds[0]
            m = re.search("Now Playing: (.*)Artist Link", np.get_text())
            text = m.group(1)
            artist, track = text.split(" - ", 1)
            self.d.now_playing("Radio Free Fedi", artist, track)
            time.sleep(10)

if __name__ == "__main__":
    np = NP()
    np.run()
