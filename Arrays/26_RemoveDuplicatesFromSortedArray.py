'''

LeetCode 26: Remove Duplicates from Sorted Array
Approach: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)

Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.

The relative order of the elements should be kept the same.

Return k after placing the first k unique elements in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,2]
Output: 2
nums = [1,2,_]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5
nums = [0,1,2,3,4,_,_,_,_,_]

'''

def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j] :
            j += 1
            nums[j] = nums[i]
    return j + 1