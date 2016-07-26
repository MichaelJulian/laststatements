import pickle
from collections import Counter
from string import punctuation
statements = pickle.load(open('last_statements'))
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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

cleaned = clean_statements(statements)
trigrams = []
for statement in cleaned:
    word_list = statement.split(' ')
    trigrams.extend(zip(word_list, word_list[1:], word_list[2:]))

c = Counter(trigrams)
most_common = c.most_common(7)
num_declined = np.array(['This offender declined' in statement for statement in statements]).sum()


labels = [' '.join(l[0]) for l in most_common]
values = [v[1] for v in most_common]
labels.append('No Statement')
values.append(num_declined)

indexes = np.arange(len(labels))
sns.barplot(indexes, values)
sns.plt.xticks(indexes, labels)
sns.plt.title('Most common 3-word phrases of Death Row Inmates\n')
plt.ylabel('Count')
plt.xlabel('Phrase')
plt.savefig('ngram_7.png')
plt.show()
