# Write your MySQL query statement below
select orders.customer_number
from orders 
GROUP BY CUSTOMER_NUMBER
ORDER BY COUNT(CUSTOMER_NUMBER)DESC
LIMIT 1;