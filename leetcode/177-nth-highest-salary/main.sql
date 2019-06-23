-- CREATE FUNCTION is the way to create function in SQL
-- 1. DECLARE M INT; SET M=N-1;
-- offset M

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
RETURN (
  select ifnull(
      (select distinct Salary
       from Employee
       order by Salary desc
       limit 1
       offset M
      ),
      null
  )
);
END