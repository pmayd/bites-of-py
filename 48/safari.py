import os
import urllib.request
import re
from collections import defaultdict

LOG = os.path.join('tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'

if not os.path.exists(LOG):
    urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def create_chart():
    books_per_day = defaultdict(list)
    isbn = re.compile(r'([\dA_Z]{10,13})')

    # parse log for new books
    with open(LOG, 'r', encoding='utf-8') as logfile:

        for line in logfile:
            date = line.split()[0]

            # either add new book or check if previous book is cached
            if re.search(isbn, line):
                token = PY_BOOK if 'python' in line.lower() else OTHER_BOOK

            elif not 'cached, skipping' in line.lower():
                books_per_day[date] += token
       
    # print chart
    for day, books in books_per_day.items():
        print(f'{day} {"".join(books)}')            


if __name__ == "__main__":
    print(create_chart())