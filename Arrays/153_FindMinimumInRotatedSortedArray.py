'''

LeetCode 153: Find Minimum in Rotated Sorted Array
Approach: Binary Search on Rotated Sorted Array
Time Complexity: O(log n)
Space Complexity: O(1)

Given a sorted array nums of unique elements that has been rotated
between 1 and n times, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0

Example 3:
Input: nums = [11,13,15,17]
Output: 11

'''

def findMin(nums):
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
        