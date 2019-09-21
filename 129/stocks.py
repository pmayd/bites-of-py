import requests
from collections import Counter

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program
with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:
def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0

    elif 'M' in cap:
        return float(cap[1:-1])

    elif 'B' in cap:
        return float(cap[1:-1]) * 1e3


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    cap_for_industry = [_cap_str_to_mln_float(e['cap']) for e in data if e['industry'] == industry]

    return round(sum(cap_for_industry), 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    # assumption: each entry comes only once
    symbol_with_cap = [(e['symbol'], _cap_str_to_mln_float(e['cap'])) for e in data]

    return sorted(symbol_with_cap, key=lambda x: x[1], reverse=True)[0][0]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    c = Counter([e['sector'] for e in data if e['industry'] != 'n/a'])

    return c.most_common(1)[0][0], c.most_common()[-1][0]


if __name__ == "__main__":
    pass