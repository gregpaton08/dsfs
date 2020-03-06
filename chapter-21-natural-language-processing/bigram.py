#!/usr/bin/env python3

import web_scrape
from collections import defaultdict
import random
from typing import List

words = web_scrape.scrape()

pairs = defaultdict(list)
for prev, current in zip(words, words[1:]):
    pairs[prev].append(current)

current = "."
sentence: List[str] = []
while True:
    possible_words = pairs[current]
    current = random.choice(possible_words)
    sentence.append(current)
    if current == ".":
        break

print(" ".join(sentence))
