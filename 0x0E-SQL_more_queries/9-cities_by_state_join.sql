-- lists all cities contained in the database hbtn_0d_usa
SELECT
	c.id as id,
	c.name as name,
	s.name as name
FROM cities c
JOIN states s ON c.state_id = s.id;

