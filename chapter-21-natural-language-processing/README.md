# Chapter 21 - Natural Language Processing

## Word Clouds

Look cool, largely useless. One useful approach would be to use the axes of the plot to convey some information, e.g. word higher on the Y axis indicates higher frequency of occurrence of words on a resume and higher on the X axis means higher frequency of occurrence for the same word on job postings.

## n-Gram Language Models

A method for modeling language to generate text.

Using a [corpus](../glossary.md#corpus) of documents generate a statistical model of language and use it to generate "original" text documents.

### Bigram (n = 2)

Using the data generate pairs of consecutive words. To create a new sentence, start with any "starting" word, that is, and word preceded by a period. From the set of words that follow the current word, shoose one at random. Continue this process until a period is found.

```python
def bigram(consecutive_words: Dict[str, List[str]]) -> str:
    setence: List[str] = []
    current_word = "."
    while True:
        current_word = \
            random.choice(consecutive_words[current_word])
        sentence.append(current_word)
        if current_word == ".":
            break

    return " ".join(sentence)
```

### Trigram (n = 3)

Similar to bigrams except uses triplets of words instead of pairs. Produces better sounding text, largely due to the fact that there are fewer random choices to make, so many of the genereated sentences and phrases are verbatim to the original text. Increasing the corpus size would help with this.

```python
def trigram(triplets: Dict[Tuple[str, str], str]) -> str:
    sentence: List[str] = []
    starting_words = [key[1] if key[0] == "." for key in triplets]
    current: Tuple[str, str] = (".", random.choice(starting_words))
    while True:
        sentence.append(current[1])
        if len(triplets[current]) == 0 or sentence[-1] == ".":
            break
        current = (current[1], random.choice(triplets[current]))

    return " ".join(sentence)
```

## Grammars

