/*
 * @lc app=leetcode id=1480 lang=javascript
 *
 * [1480] Running Sum of 1d Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function (nums) {
  // Method 1
  const length = nums.length;
  let index = 1;
  if (length <= 1) {
    return nums;
  }
  while (index < length) {
    nums[index] = nums[index] + nums[index - 1];
    console.log(nums[index]);
    index += 1;
  }
  return nums;
};
// @lc code=end
