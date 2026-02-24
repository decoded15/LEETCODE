'''
LeetCode: How Many Numbers Are Smaller Than the Current Number
Approach: Brute Force (Nested Loop)
Time Complexity: O(n^2)
Space Complexity: O(1)

Given an array nums, for each nums[i], count how many numbers
in the array are strictly smaller than it.

For every element, iterate through the entire array and
count elements smaller than the current element.

Return the result as an array.
'''

def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        for i in range(len(nums)) :
            c = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i] :
                    c += 1
            res[i] = c
        return res