from collections import Counter, defaultdict
import csv
import re
import requests
import string 

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    dict_of_words_per_character_and_episode = defaultdict(Counter)

    reader = csv.DictReader(content.split("\n"))
    
    for row in reader:
        episode = row['Episode']
        char = row['Character']
        line = row['Line']

        if line:
            words = line.split()
            dict_of_words_per_character_and_episode[char].update({episode: len(words)})

    return dict_of_words_per_character_and_episode

if __name__ == "__main__":
    content = get_season_csv_file(season=1)
    
    print (re.findall(r'(?:1,9,Cartman,)(".*)', content))
    dict = get_num_words_spoken_by_character_per_episode(content)

    print(dict['Cartman'])
