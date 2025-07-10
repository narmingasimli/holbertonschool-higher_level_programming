-- score and name in MySQL
SELECT
	score,
	name 
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
