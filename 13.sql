SELECT distinct(name) FROM people
JOIN stars on people.id = stars.person_id
JOIN movies on stars.movie_id = movies.id
WHERE movies.title IN(
    SELECT distinct(movies.title) FROM people
    JOIN stars on people.id = stars.person_id
    JOIN movies on stars.movie_id = movies.id
    WHERE people.name = "Kevin Bacon" AND people.birth = 1958) AND people.name != "Kevin Bacon"