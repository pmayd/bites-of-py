# Bite 30. Movie data analysis

In this Bite we are going to parse a csv movie dataset to identify the directors with the highest rated movies.

1. Write `get_movies_by_director`: use `csv.DictReader` to convert __movie_metadata.csv__ into a `(default)dict` of `list`s of **Movie** `namedtuples`. Convert/filter the data:
    - Only extract director_name, movie_title, title_year and imdb_score.
    - Type conversions: `title_year` -> `int` / `imdb_score` -> `float`
    - **Discard any movies older than 1960**.

    Here is an extract:
    ```json
    ....
    { 'Woody Allen': [
        Movie(title='Midnight in Paris', year=2011, score=7.7),
        Movie(title='The Curse of the Jade Scorpion', year=2001, score=6.8),
        Movie(title='To Rome with Love', year=2012, score=6.3),  ....
        ], ...
    }
    ```

2. Write the `calc_mean_score` helper that takes a list of Movie `namedtuples` and calculates the mean IMDb score, returning the score rounded to 1 decimal place.
3. Complete `get_average_scores` which takes the directors data structure returned by `get_movies_by_director` (see 1.) and returns a list of `tuple`s `(director, average_score)` ordered by highest score in **descending order**. Only take directors into account with >= `MIN_MOVIES`

See the tests for more info. This could be tough one, but we really hope you learn a thing or two. Good luck and keep calm and code in Python!
