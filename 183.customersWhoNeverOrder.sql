--
-- @lc app=leetcode id=183 lang=mysql
--
-- [183] Customers Who Never Order
--

-- @lc code=start
# Write your MySQL query statement below

-- Method 1 (left join)
-- select name as Customers 
-- from 
-- Customers cust left join Orders ord 
-- on cust.id = ord.customerId
-- where customerId is null;

-- Method 2

select name as Customers 
from Customers where 
id not in 
(select customerId from Orders);


-- @lc code=end

