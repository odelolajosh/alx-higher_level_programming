-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT g.name, SUM(sr.rate) AS `rating sum` FROM tv_genres g
JOIN tv_show_genres tv ON g.id = tv.genre_id
JOIN tv_show_ratings sr ON sr.show_id = tv.show_id
GROUP BY g.name
ORDER BY `rating sum` DESC
