'''

LeetCode 33: Search in Rotated Sorted Array
Approach: Binary Search with Sorted Half Detection
Time Complexity: O(log n)
Space Complexity: O(1)

You are given an integer array nums sorted in ascending order,
then rotated at some unknown pivot. All elements are unique.

Given a target value, return its index if found.
If not found, return -1.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''

def search(nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1