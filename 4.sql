SELECT COUNT(title) FROM MOVIES
JOIN ratings on movies.id = ratings.movie_id
WHERE rating == 10