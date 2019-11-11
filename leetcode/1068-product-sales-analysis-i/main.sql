-- 1st: left join
-- 2899 ms, faster than 5.02%
SELECT Product.product_name, Sales.year, Sales.price
FROM Product
INNER JOIN Sales
ON Product.product_id = Sales.product_id

-- 2nd: just select from
SELECT Product.product_name, Sales.year, Sales.price
FROM Product, Sales
WHERE Product.product_id = Sales.product_id