'''

LeetCode 496: Next Greater Element I
Approach: Monotonic Decreasing Stack + Hash Map
Time Complexity: O(n)
Space Complexity: O(n)

You are given two arrays nums1 and nums2 where nums1 is a subset of nums2.
For each element in nums1, find the next greater element to its right in nums2.
If no such element exists, return -1.

Example:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

'''

def nextGreaterElement(nums1, nums2):
        stack = []
        next_greater = {}
        for num in nums2 :
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        while stack :
            next_greater[stack.pop()] = -1
        
        l = [next_greater[num] for num in nums1]

        return l