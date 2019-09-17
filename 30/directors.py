import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = 'tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)

if not os.path.exists(local):
    urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies = defaultdict(list)
    with open(local, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for movie in reader:
            movie_year = int(movie['title_year']) if movie['title_year'] else -1
            movie_director = movie['director_name']
            movie_title = movie['movie_title']
            movie_score = float(movie['imdb_score'])

            if movie_year >= 1960:
                movies[movie_director].append(
                    Movie(movie_title, movie_year, movie_score))

    return movies
        

def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    mean_score = 0
    for movie in movies:
        mean_score += movie.score
    
    return round(mean_score / len(movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    list_of_directors_and_scores = [(d, calc_mean_score(movies)) for d, movies in directors.items() if len(movies) >= MIN_MOVIES]
    sorted_list_of_directors_and_scores = sorted(list_of_directors_and_scores, key=lambda x: x[1], reverse=True)

    return sorted_list_of_directors_and_scores


if __name__ == "__main__":
    print(get_movies_by_director())