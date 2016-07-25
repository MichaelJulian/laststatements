import pickle
from collections import Counter
from string import punctuation
statements = pickle.load(open('last_statements'))
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment import SentimentIntensityAnalzyer
from nltk import tokenize

def clean_word(word):
    word = word.strip()
    word = word.replace('\r\n', ' ')
    word = word.replace("'", '')
    word = word.replace("\u2019", '')
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.strip(punctuation)
    return word

def clean_statements(statements):
    cleaned = []
    for statement in statements:
        if 'This offender declined' in statement:
            pass
        else:
            cleaned.append(' '.join([clean_word(word) for word in statement.split(' ')]))
    return cleaned

sentences = []
cleaned = clean_statements(statements)
lines_list = tokenize.sent_tokenize(cleaned)
sentences.extend(lines_list)
sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    
