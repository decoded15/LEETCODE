'''

LeetCode 238: Product of Array Except Self
Approach: Prefix & Suffix Product (Without Division)
Time Complexity: O(n)
Space Complexity: O(1) [excluding output array]

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''

def ProductExceptSelf(nums):
    n = len(nums)
    answer = []
    
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer