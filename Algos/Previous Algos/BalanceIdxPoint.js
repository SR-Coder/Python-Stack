/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

const nums3 = [9,1,1,1,1,7,3,6,1,3]
const expected3 = 5
/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @return {number} The balance index or -1 if there is none.
 */
/**
 * - Time: O(2n) linear -> O(n).
 * - Space: O(1) constant.
 */
 function balanceIndex(nums) {
  if (nums.length < 3) {
    return -1;
  }

  let left = nums[0];
  let right = 0;

  for (let i = 2; i < nums.length; i++) {
    right += nums[i];
  }

  for (let i = 1; i < nums.length - 1; i++) {
    if (left === right) {
      return i;
    }

    right -= nums[i + 1];
    left += nums[i];
  }
  return -1;
}

/**
 * - Time: O(n/2) -> O(n) linear, n/2 since looping from outside towards center.
 * - Space: O(1) constant.
 */
function balanceIndexOutsideIn(nums) {
  if (nums.length < 3) {
    return -1;
  }
  let leftIdx = 0;
  let rightIdx = nums.length - 1;
  let leftSum = 0;
  let rightSum = 0;

  while (leftIdx < rightIdx) {
    if (nums[leftIdx] == 0) {
      leftIdx++;
      continue;
    }
    if (nums[rightIdx] == 0) {
      rightIdx--;
      continue;
    }
    if (leftSum == rightSum) {
      leftSum += nums[leftIdx];
      rightSum += nums[rightIdx];
      leftIdx++;
      rightIdx--;
    } else if (leftSum < rightSum) {
      leftSum += nums[leftIdx];
      leftIdx++;
    } else {
      rightSum += nums[rightIdx];
      rightIdx--;
    }
  }

  if (leftSum == rightSum && leftIdx == rightIdx) {
    return leftIdx;
  } else {
    return -1;
  }
}

module.exports = { balanceIndex };

/*****************************************************************************/

/* 
  Balance Point
  Write a function that returns whether the given
  array has a balance point BETWEEN indices, 
  where one side’s sum is equal to the other’s. 
*/

const nums1 = [1, 2, 3, 4, 10];
const expected1 = true;
// Explanation: between indices 3 & 4

const nums2 = [1, 2, 4, 2, 1];
const expected2 = false;

/**
 * Determines if there is a balance point BETWEEN indexes where the sum of the
 *    left side is equal to the sum of the right side of the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @return {boolean} Indicates if a balance point exists.
 */
/**
 * - Time: O(2n) -> O(n) linear.
 * - Space: O(1) constant.
 */
 function balancePoint(nums) {
  const length = nums.length;

  if (length < 2) {
    return false;
  }

  let left = nums[0];
  let right = 0;

  for (let i = 1; i < length; i++) {
    right += nums[i];
  }

  for (let i = 1; i < length; i++) {
    if (left === right) {
      return true;
    }

    right -= nums[i];
    left += nums[i];
  }
  return false;
}

/**
 * https://leetcode.com/problems/partition-equal-subset-sum/
 * Dynamic programming bonus: can any order of arr result in a balance point
 * start with 0, add and subtract first num to 0 and save results on every
 * subsequent num, add and subtract it to each previous result check at the
 * end if a 0 exists due to one of the sums or differences cancelling out.
 */
function isBalancePointPossible(nums) {
  const calcs = { "-1": new Set().add(0) };

  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    calcs[i] = new Set();

    for (const prevCalc of calcs[i - 1]) {
      calcs[i].add(prevCalc + n);
      calcs[i].add(prevCalc - n);
    }
  }
  return calcs[nums.length - 1].has(0);
}

module.exports = { balancePoint };

/*****************************************************************************/