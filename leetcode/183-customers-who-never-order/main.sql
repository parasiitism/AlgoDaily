-- SQL: not in
select Customers.Name as Customers
from Customers 
where Customers.id
not in (
    select CustomerId from Orders
)

-- SQL: left join with null
SELECT Customers.Name as Customers
from Customers
LEFT JOIN Orders
on  Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId is NULL 