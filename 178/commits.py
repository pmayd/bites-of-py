from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join('tmp', 'commits')

if not os.path.exists(commits):
    urlretrieve('https://bit.ly/2H1EuZQ', commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    c = Counter()
    with open(commit_log, 'r', encoding='utf-8') as log:
        for line in log:
            log_year = int(line.split()[5])

            if year is not None and log_year != year:
                continue
            
            # parse line
            log_date = parse(" ".join(line.split()[1:6]))
            insertions = int(line.split(",")[1].split()[0]) if 'insertions(+)' in line.split(",")[1] else 0
                
            if len(line.split(",")) == 2:
                deletions = int(line.split(",")[1].split()[0]) if 'deletions(-)' in line.split(",")[1] else 0
            else:
                deletions = int(line.split(",")[2].split()[0]) if 'deletions(-)' in line.split(",")[2] else 0


            # add entry
            key = YEAR_MONTH.format(y=log_date.year, m=log_date.month)
            c += Counter({key: insertions - deletions})

    return c.most_common()[-1][0], c.most_common(1)[0][0]


if __name__ == "__main__":
    print(get_min_max_amount_of_commits())        




