#!/usr/bin/env python3

import web_scrape
from collections import defaultdict
import random
from typing import Dict, List, Tuple

words: List[str] = web_scrape.scrape()
starting_words: List[str] = []
trigrams: Dict[Tuple[str, str], str] = defaultdict(list)
for prev, current, next in zip(words, words[1:], words[2:]):
    if prev == ".":
        starting_words.append(current)
    
    trigrams[(prev, current)].append(next)

sentence: List[str] = []
current: Tuple[str, str] = (".", random.choice(starting_words))
while True:
    sentence.append(current[1])
    if len(trigrams[current]) == 0:
        break
    current = (current[1], random.choice(trigrams[current]))
    if current[1] == ".":
        break

print(" ".join(sentence))
