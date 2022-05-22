from datetime import datetime

import pandas as pd
import numpy as np
import spacy as spacy
import regex as re
import json

from utils import levenshtein_distance

sentence_limit = 10000

input_path = '../../res/news.2021.en.shuffled.deduped'
output_path = 'levensthein_' + str(sentence_limit) + '_set.json'
input_example = 'example.txt'
output_example = 'example_out.json'

spacy_en = spacy.load('en_core_web_lg')
english_word_regex = r"([A-Z]|[a-z]|')"


def max_distance_criterium(word1, word2):
    max_distance = 3
    if len(word1) <= 2 or len(word2) <= 2:
        max_distance = 2
    return max_distance


start = datetime.now()


def create_set(input_file, output_file, sentence_limit):
    # dict containing word as a key, and confusing words as a value
    new_confusion_dict = {}
    unique_words = set()
    with open(input_file, encoding="utf-8") as f:
        print("Reading a file...")
        for i in range(sentence_limit):
            # reading all the file at once may end in memory error
            line = f.readline()
            if not line:
                break
            line = line[:-2]    # remove \n
            list_of_words = [tok.text for tok in spacy_en.tokenizer(line)]
            for word in list_of_words:
                if re.match(english_word_regex, word):
                    unique_words.add(word)

    print("Create dictionary...")

    unique_words_list = list(unique_words)
    for i in range(len(unique_words_list) - 1):
        if i % 1000 == 0:
            print("already processed " + str(i) + " words...")
        confusion_list = []
        if len(unique_words_list[i]) < 2:
            continue
        for j in range(len(unique_words_list) - 1):
            if len(unique_words_list[j]) < 2:
                continue
            if i != j and levenshtein_distance(unique_words_list[i], unique_words_list[j]) < \
                    max_distance_criterium(unique_words_list[i], unique_words_list[j]):
                confusion_list.append(unique_words_list[j])
        new_confusion_dict[unique_words_list[i]] = confusion_list

    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(json.dumps(new_confusion_dict))


create_set(input_path, output_path, sentence_limit)
# create_set(input_example, output_example, sentence_limit)
print("Process took: " + str(datetime.now() - start))
