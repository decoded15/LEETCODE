'''

LeetCode 189: Rotate Array
Approach: In-place Array Reversal
Time Complexity: O(n)
Space Complexity: O(1)

Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

You must do this in-place with O(1) extra space.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

'''

def rotate(self, nums, k):
    n = len(nums)
    k = k % n

    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
