-- lists all shows without the genre Comedy
SELECT tv_shows.title FROM tv_shows
LEFT JOIN (
    SELECT s.id, g.name FROM tv_shows s
    JOIN tv_show_genres tv ON tv.show_id = s.id
    JOIN tv_genres g ON g.id = tv.genre_id
    WHERE g.name = "Comedy"
) c ON c.id = tv_shows.id
WHERE c.name IS NULL 
ORDER BY tv_shows.title;