#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re
from typing import List

def scrape(url: str ="https://gregpaton08.com/") -> List[str]:
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    content = soup.find("div", "home")

    regex = r"[\w']+|[\.]"
    words = []
    for paragraph in content("p"):
        words.extend(re.findall(regex, paragraph.text))
    return words

if __name__ == "__main__":
    print(scrape())
