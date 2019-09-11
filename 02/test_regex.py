from regex import (extract_course_times,
                   get_all_hashtags_and_links,
                   match_first_paragraph)
import pytest


def test_extract_course_times_default_arg():
    expected = ['01:47', '32:03', '41:51', '27:48', '05:02']
    assert extract_course_times() == expected


def test_get_all_hashtags_and_links_default_arg():
    expected = ['http://pybit.es/requests-cache.html', '#python', '#APIs']
    assert get_all_hashtags_and_links() == expected


def test_match_first_paragraph_default_arg():
    expected = 'pybites != greedy'
    assert match_first_paragraph() == expected


def test_extract_course_times_other_course_input():
    course = ('0:40 Lesson introduction'
              '1:33 Your 3 day overview'
              '8:12 Learning datetime and date'
              '6:07 Datetime timedelta usage'
              '4:02 Concepts: what did we learn')
    expected = ['0:40', '1:33', '8:12', '6:07', '4:02']
    assert extract_course_times(course) == expected


def test_get_all_hashtags_and_links_other_tweet():
    tweet = ('PyBites My Reading List | 12 Rules for Life - #books '
             'that expand the mind! '
             'http://pbreadinglist.herokuapp.com/books/'
             'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter'
             ' #psychology #philosophy')
    expected = ['#books',
                ('http://pbreadinglist.herokuapp.com/books/'
                 'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter'),
                '#psychology', '#philosophy']
    assert get_all_hashtags_and_links(tweet) == expected


def test_match_first_paragraph_other_html():
    html = ('<p>Match only this paragraph.</p>'
            '<p>Not this one!</p><p>And this one neither.</p>')
    expected = 'Match only this paragraph.'
    assert match_first_paragraph(html) == expected


if __name__ == "__main__":
    pytest.main()