SELECT name FROM people
JOIN directors ON people.id = directors.person_id
JOIN ratings ON directors.movies_id = ratings.movie_id
WHERE ratings.rating >= 9.0