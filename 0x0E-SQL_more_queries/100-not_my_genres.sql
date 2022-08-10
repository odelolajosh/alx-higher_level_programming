-- list all genres not linked to the show Dexter
SELECT DISTINCT genre.name FROM tv_genres genre
LEFT JOIN (
    SELECT g.id FROM tv_show_genres tv
    JOIN tv_genres g ON g.id = tv.genre_id
    JOIN tv_shows s ON s.id = tv.show_id
    WHERE s.title = "Dexter"
) d ON d.id = genre.id
WHERE d.id is NULL
ORDER BY genre.name;
