'''

LeetCode 724: Find Pivot Index
Approach: Prefix Sum / Running Sum
Time Complexity: O(n)
Space Complexity: O(1)

Given an array of integers nums, calculate the pivot index such that
the sum of elements to the left of the index is equal to the sum of
elements to the right.

If no such index exists, return -1.

'''
def pivotIndex(nums):
        for i in range(len(nums)):
            if (sum(nums[0:i]) == sum(nums[i+1 : len(nums)])):
                return i
        return -1