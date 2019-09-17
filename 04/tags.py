from pathlib import Path
from collections import Counter
import urllib.request

import xml.etree.ElementTree as ET


# prep
tempfile = Path('tmp').joinpath('feed.xml')

if not tempfile.parent.exists():
    tempfile.parent.mkdir()

if not tempfile.exists():
    tempfile.touch()
    urllib.request.urlretrieve('http://bit.ly/2zD8d8b', str(tempfile))

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    root = ET.fromstring(content)

    categories = []
    for item in root[0].findall('item'):
        for category in item.findall('category'):
            categories.append(category.text)

    return Counter(categories).most_common(n)


if __name__ == "__main__":
    print(get_pybites_top_tags())