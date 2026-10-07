# Write your MySQL query statement below
SELECT pt.PRODUCT_NAME,st.YEAR,st.PRICE FROM SALES ST
 JOIN PRODUCT pt on st.product_id = pt.product_id;