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
        name == "Post Malone"
)