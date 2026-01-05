'''

LeetCode 27: Remove Element
Approach: Two Pointers (Swap with End)
Time Complexity: O(n)
Space Complexity: O(1)

Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place.

The order of the elements may be changed.
Return the number of elements in nums which are not equal to val.

The first k elements of nums should contain the final result.
It does not matter what you leave beyond the first k elements.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2
nums = [2,2,_,_]

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5
nums = [0,1,3,0,4,_,_,_]

'''

def removeElement(nums, val):
    l = 0
    r = len(nums) - 1

    while l <= r:
        if nums[l] != val:
            l += 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1

    return r + 1
