import pandas as pd
import numpy as np
import spacy as spacy
import regex as re
import string

from utils import levenshtein_distance

input_path = '../../res/news.2021.en.shuffled.deduped'
sentence_limit = 100000000
spacy_en = spacy.load('en_core_web_lg')
english_word_regex = r"([A-Z]|[a-z]|')"



def confuse(word, confusion_set, probability):
    return word

sentences_with_errors = []

with open(input_path, encoding="utf-8") as f:
    for i in range(sentence_limit):
        sentence = f.readline()
        list_of_words = [tok.text for tok in spacy_en.tokenizer(sentence)]
        for word in list_of_words:
            if re.match(english_word_regex, word):
                pass
                # word = confuse(word, confusion_set, probability)
        print(' '.join(list_of_words))
        sentences_with_errors.append(' '.join(list_of_words))

