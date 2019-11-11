-- 1st: ternary function in SQL
-- IF(expression, <true result>, <false result>)
SELECT x, y, z, IF(x + y > z and x + z > y and y + z > x, "Yes", "No") AS "triangle"
FROM triangle

-- 2nd: CASE expression
-- CASE WHEN expression THEN <true result> ELSE <false_result> END
SELECT x, y, z, (CASE WHEN x + y > z and x + z > y and y + z > x THEN "Yes" ELSE "No" END) AS "triangle"
FROM triangle