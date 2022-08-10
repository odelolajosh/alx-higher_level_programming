-- lists all Comedy shows
SELECT s.title FROM tv_show_genres tv
JOIN tv_shows s ON s.id = tv.show_id
JOIN tv_genres g ON g.id = tv.genre_id
WHERE g.name = "Comedy"
ORDER BY s.title
