'''

LeetCode 162: Find Peak Element
Approach: Binary Search on Slope
Time Complexity: O(log n)
Space Complexity: O(1)

A peak element is an element that is strictly greater than its neighbors.
The array edges are considered to have -∞ beyond boundaries.

Return any peak index.

Example:
Input: nums = [1,2,3,1]
Output: 2

'''
def findPeakElement(nums):
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low
        