SELECT name FROM people
JOIN stars on people.id = people_id
JOIN movies on movie.id = movies_id
WHERE movies.title = "Toy Story"