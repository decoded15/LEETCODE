'''

LeetCode 34: Find First and Last Position of Element in Sorted Array
Approach: Binary Search (Two Passes)
Time Complexity: O(log n)
Space Complexity: O(1)

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''
def searchRange(nums, target):
        def findFirst():
            low, high = 0, len(nums) - 1
            first = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return first

        def findLast():
            low, high = 0, len(nums) - 1
            last = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return last

        return [findFirst(), findLast()]