-- score and name in MySQL
SELECT
	score,
	name IS NOT NULL
FROM second_table
ORDER BY score DESC;
