-- lists the number of records with the same score in the table second_table
-- of the database hbtn_0c_0 in your MySQL server.
SELECT DISTINCT score COUNT(*) AS number
    FROM second_table
    ORDER BY score DESC;
