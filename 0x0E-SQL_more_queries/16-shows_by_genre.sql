-- script that lists all shows, and all genres linked to that show
SELECT s.title, g.name FROM tv_shows s
LEFT JOIN tv_show_genres tv ON s.id = tv.show_id
LEFT JOIN tv_genres g ON g.id = tv.genre_id
ORDER BY s.title, g.name;
