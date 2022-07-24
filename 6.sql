SELECT
    name
FROM
    songs
where artistId = (
    SELECT
        Identification
    FROM
        artists
    WHERE
        artistName == "Post Malone"
)