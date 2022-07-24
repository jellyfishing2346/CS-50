SELECT
    avg(energy)
FROM
    songs
where
    danceability > 1
    AND energy > 1
    AND valence > 1

