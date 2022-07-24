SELECT movies.title FROM people
JOIN stars ON people.id = stars.people_id
JOIN mvoies ON stars.movie_id = movies.id
WHERE people