/*
 * @lc app=leetcode id=283 lang=javascript
 *
 * [283] Move Zeroes
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  const len = nums.length;
  let [nonZeroIndex, zeroIndex] = [0, 0];
  while (nonZeroIndex < len) {
    if (nums[nonZeroIndex] != 0) {
      const temp = nums[zeroIndex];
      nums[zeroIndex] = nums[nonZeroIndex];
      nums[nonZeroIndex] = temp;
      zeroIndex += 1;
    }
    nonZeroIndex += 1;
  }
};
// @lc code=end
