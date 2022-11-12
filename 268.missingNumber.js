/*
 * @lc app=leetcode id=268 lang=javascript
 *
 * [268] Missing Number
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  const len = nums.length;
  const actualSum = (len * (len + 1)) / 2;
  let arraySum = 0;
  //   nums.map((num) => arraySum + num);
  nums.forEach((num) => {
    arraySum = arraySum + num;
  });
  console.log(arraySum, actualSum);
  return actualSum - arraySum;
};
// @lc code=end
