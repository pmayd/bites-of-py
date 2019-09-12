from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    automakers_and_number_models_in_year = dict([
        (e['automaker'], len(get_models(e['automaker'], year)))
        for e in data if e['year'] == year
    ])

    return Counter(automakers_and_number_models_in_year).most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return set([e['model'] for e in data if e['year'] == year and e['automaker'] == automaker])


if __name__ == "__main__":
    print(get_models('Chrysler', 2002))
    print(most_prolific_automaker(2000))