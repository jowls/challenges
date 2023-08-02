-- 175. Combine Two Tables #mssql
Select  p.firstName, p.lastName, a.city, a.state from person p left join address a on p.personID = a.personID;

-- 176. Second Highest Salary #mssql
select max(salary) SecondHighestSalary from employee where salary < (select max(salary) from employee);

--only slightly faster #mssql
select isnull((select distinct salary from employee order by salary desc offset 1 rows fetch next 1 rows only), null) as SecondHighestSalary;

-- 177. Nth Highest Salary #mssql
CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        select isnull((select distinct salary from employee order by salary desc offset @n-1 rows fetch next 1 rows only), null)
    );
END

-- 182. Duplicate Emails #mssql #oracle
select Email from Person group by Email having count(Email) > 1;

-- 183. Customers Who Never Order #mssql
select c.name Customers from customers c left join orders o on c.id = o.customerId where o.customerId is null;

-- 577. Employee Bonus  #mssql
select e.name, b.bonus from employee e left join bonus b on e.empId = b.empId where b.bonus < 1000 or b.bonus is null;

