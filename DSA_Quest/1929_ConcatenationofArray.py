'''
1929. Concatenation of Array

Problem:
Given an integer array nums of length n,
create an array ans of length 2n where:
ans[i] = nums[i]
ans[i + n] = nums[i]

In short:
Return nums concatenated with itself.

Approach:
• Use Python list multiplication.
• nums * 2 duplicates the list.
• Return the new list.

Time Complexity: O(n)
Space Complexity: O(n)

'''

def getConcatenation(nums):
        nums2 = nums * 2
        return nums2