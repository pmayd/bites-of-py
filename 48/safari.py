import os
import urllib.request

LOG = os.path.join('tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'

if not os.path.exists(LOG):
    urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def create_chart():
    pass


if __name__ == "__main__":
    print(create_chart())