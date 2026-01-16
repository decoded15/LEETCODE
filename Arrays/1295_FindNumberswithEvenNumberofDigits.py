'''

LeetCode 1295: Find Numbers with Even Number of Digits
Approach: Linear Search with String Conversion
Time Complexity: O(n)
Space Complexity: O(1)

Given an array of integers nums, return how many of them contain
an even number of digits.

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2

Example 2:
Input: nums = [555,901,482,1771]
Output: 1

'''

def findNumbers(nums):
    count = 0

    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1

    return count