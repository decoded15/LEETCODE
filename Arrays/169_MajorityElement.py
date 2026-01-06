'''

LeetCode 169: Majority Element
Approach: Hash Map (Frequency Counting)
Time Complexity: O(n)
Space Complexity: O(n)

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''

def majorityElement(self, nums):
    me = nums[0]
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

        if freq[num] > (len(nums) / 2):
            me = num

    return me
