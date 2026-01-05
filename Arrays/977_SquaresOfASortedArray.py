'''

LeetCode 977: Squares of a Sorted Array

This file contains TWO approaches:
1. Simple Approach (Square + Sort)
2. Optimized Approach (Two Pointers)

----------------------------------
Approach 1: Square + Sort
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach 2: Two Pointers
Time Complexity: O(n)
Space Complexity: O(n)

----------------------------------

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

'''

#Approach 1
class Solution(object):
    def sortedSquares(self, nums):
        squared = [x * x for x in nums]
        return sorted(squared)

#Approach 2
class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1

        return result