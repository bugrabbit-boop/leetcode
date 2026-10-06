# Write your MySQL query statement below
SELECT euni.unique_id,e.name from EMPLOYEES E
LEFT JOIN EMPLOYEEUNI euni
on e.id = euni.id;