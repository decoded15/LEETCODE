'''

LeetCode 283: Move Zeroes
Approach: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: nums = [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: nums = [0]

'''
def moveZeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j+=1
    return nums