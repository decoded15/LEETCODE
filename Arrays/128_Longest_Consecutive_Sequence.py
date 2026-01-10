'''

LeetCode 128: Longest Consecutive Sequence
Approach: HashSet + Sequence Start Detection
Time Complexity: O(n)
Space Complexity: O(n)

Given an unsorted array of integers nums, return the length of the
longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

'''
class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                count = 1

                while current + 1 in num_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest
