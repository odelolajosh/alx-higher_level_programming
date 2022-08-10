-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT s.title, MAX(r.rate) as rating FROM tv_show_ratings r
JOIN tv_shows s ON s.id = r.show_id
GROUP BY s.title
ORDER BY r.rate DESC