'''

LeetCode 268: Missing Number
Approach: Math (Sum Formula)
Time Complexity: O(n)
Space Complexity: O(1)

Given an array nums containing n distinct numbers taken from the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2

Example 2:
Input: nums = [0,1]
Output: 2

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

'''

def missingNumber(nums):
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    s = sum(nums)
    if s != expected_sum:
        return expected_sum - s