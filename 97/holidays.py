from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join("tmp", "us_holidays.php")
urlretrieve("https://bit.ly/2LG098I", holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    holidays = defaultdict(list)

    bs = BeautifulSoup(content)
    table = bs.find('table',  attrs={"class": "list-table"})
    body = table.find('tbody')
    rows = body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        month = row.find('time')['datetime'].split("-")[1]
        holiday = cols[3].text.strip()

        holidays[month].append(holiday)

    return holidays


if __name__ == "__main__":
    print(get_us_bank_holidays())