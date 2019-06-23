-- 1st approach: Left JOIN + explicit table name
-- 243 ms, faster than 23% 
select Person.FirstName, Person.LastName, Address.City, Address.State
from Person
left join Address
on Address.PersonId = Person.PersonId

-- 1st approach: Left JOIN  + implicit table name
-- 220 ms, faster than 59.65% 
select FirstName, LastName, City, State
from Person
left join Address
on Address.PersonId = Person.PersonId