from marvel import (most_popular_characters,
                    max_and_min_years_new_characters,
                    percentage_female)

import pytest, sys


def test_most_popular_characters():
    expected = ['Spider-Man', 'Captain America', 'Wolverine',
                'Iron Man', 'Thor']
    assert most_popular_characters() == expected


def test_max_and_min_years_new_characters():
    assert max_and_min_years_new_characters() == ('1993', '1958')


def test_percentage_female():
    assert percentage_female() == 23.43


if __name__ == "__main__":
    pytest.main(sys.argv)