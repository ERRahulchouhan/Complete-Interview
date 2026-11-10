
select * from employe where salary = select MAX(salary) from employee

select salary from employee order by salary desc limit n-1 ,1;

suppoise two employee max salary

select * from salary where salary = select disnict salary from employee 
order by salary desc limit n-1,1

Join Query:
    
    select * from tablea  Left JOIN tableb tableb.a == tableb.a
    
**************************************
UPDATE employee
SET gender = CASE
    WHEN gender = 'male' THEN 'female'
    WHEN gender = 'female' THEN 'male'
    ELSE gender
END;