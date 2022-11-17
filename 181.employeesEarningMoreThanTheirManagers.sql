--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
# Write your MySQL query statement below
select b.name as Employee from Employee as a join Employee as b on a.id=b.managerId
where b.salary > a.salary

-- @lc code=end

