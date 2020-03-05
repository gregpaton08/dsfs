#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re

url = "https://gregpaton08.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

# content = soup.find_all("p")
content = soup.find("div", "home")

regex = r"[\w']+|[\.]"

for paragraph in content("p"):
    words = re.findall(regex, paragraph.text)
    print(words)
