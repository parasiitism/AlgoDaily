-- 1st: left join
-- 2630 ms, faster than 5.05%
SELECT Sales.product_id, SUM(Sales.quantity) AS total_quantity
FROM Product
INNER JOIN Sales
ON Product.product_id = Sales.product_id
GROUP BY Sales.product_id
