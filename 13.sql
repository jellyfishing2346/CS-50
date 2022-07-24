SELECT distinct(name) FROM people
JOIN stars on people.id = stars.person_id
JOIN movies on stars.movie_id = movies.id
WHERE movies.title IN(
    SELECT distinct(movies.title) FROM peopl
)