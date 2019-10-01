from collections import namedtuple, Counter
import re
from typing import NamedTuple
from statistics import mean
import feedparser
from math import floor

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'http://projects.bobbelderbos.com/pcc/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}
DOMAIN_PATTERN = r'(https?://)([^/]+)'

class PythonBytes:

    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(URL)['entries']

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        return [
            e['itunes_episode'] for e in self.entries 
            if re.search(domain, e['summary'])
        ]

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        c = Counter()
        for e in self.entries:
            domains = [match.group() for match in re.finditer(DOMAIN_PATTERN, e['summary']) if match.group() not in IGNORE_DOMAINS]
            if domains:
                c.update(set(domains))

        return c.most_common(n)

    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        return len([e for e in self.entries if re.search(SPECIAL_GUEST, e['summary'])])

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        list_of_durations = []
        for e in self.entries:
            duration = e['itunes_duration']
            seconds = int(duration.split(":")[0])*3600 + int(duration.split(":")[1])*60 + int(duration.split(":")[2])
            list_of_durations.append((seconds, duration))
        
        list_of_durations = sorted(list_of_durations, key=lambda x: x[0])
        min_duration = list_of_durations[0][1]
        max_duration = list_of_durations[-1][1]
        avg = mean([d[0] for d in list_of_durations])

        return Duration(avg=floor(avg), min_=min_duration, max_=max_duration)

if __name__ == "__main__":
    pass