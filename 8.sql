SELECT name FROM people
JOIN stars on people.id = person_id
JOIN movies on movie_id = movies.id
WHERE movies.title = "Toy Story"