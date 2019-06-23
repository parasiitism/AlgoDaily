-- 1. nest query
-- 2. limit 1, 1
select ifnull(
    (select distinct Salary
    from Employee 
    order by Salary desc
    limit 1, 1),
    null
)
as SecondHighestSalary