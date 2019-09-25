import csv
from collections import defaultdict
import requests

CSV_URL = 'https://bit.ly/2HiD2i8'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    r = requests.get(CSV_URL)

    return r.text


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    countries = defaultdict(str)

    reader = csv.DictReader(content.split())

    for row in reader:
        countries[row['tz']] += '+'
    
    for country, bar in sorted(countries.items()):
        print(f'{country:20} | {bar}')


if __name__ == "__main__":
    print(create_user_bar_chart(get_csv()))