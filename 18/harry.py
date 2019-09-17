import os
import urllib.request
from collections import Counter
import string
import re

# data provided
stopwords_file = os.path.join('tmp', 'stopwords')
harry_text = os.path.join('tmp', 'harry')

if not os.path.exists(stopwords_file):
    urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)

if not os.path.exists(harry_text):
    urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)

with open(harry_text, 'r', encoding="utf8") as f:
    harry: str = f.read().lower()

with open(stopwords_file, 'r', encoding="utf8") as f:
    stopwords = f.read().lower().split("\n")

def get_harry_most_common_word():
    harry_without_punctuation = harry.translate(harry.maketrans("", "", string.punctuation))
    filtered_words = [w for w in re.split(r'\n|\s', harry_without_punctuation) if w not in stopwords and w.isalnum()]
    return Counter(filtered_words).most_common(1)[0]


if __name__ == "__main__":
    print(get_harry_most_common_word())