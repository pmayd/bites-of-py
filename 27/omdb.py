import glob
import json
import os
from urllib.request import urlretrieve
import re

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = 'tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    if not os.path.exists(local):
        urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    movies = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            movies.append(json.load(f))
    return movies


def get_single_comedy(movies):
    return [movie['Title'] for movie in movies if 'Comedy' in movie['Genre']][0]


def get_movie_most_nominations(movies):
    nominations = re.compile(r'(\d+)(?:\snominations?)')
    return max(sorted([(int(re.search(nominations, movie['Awards']).group(1)), movie['Title']) for movie in movies]))[1]


def get_movie_longest_runtime(movies):
    return max(sorted([(int(movie['Runtime'].split()[0]), movie['Title']) for movie in movies]))[1]


if __name__ == "__main__":
    movies = get_movie_data()
    print(get_single_comedy(movies))
    print(get_movie_most_nominations(movies))
    print(get_movie_longest_runtime(movies))