'''

LeetCode 350: Intersection of Two Arrays II
Approach: Hash Map (Frequency Counting)
Time Complexity: O(n + m)
Space Complexity: O(n)

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result should appear as many times as it shows in both arrays.
The result can be returned in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

'''

def intersect(nums1, nums2):
    freq = {}
    res = []

    for num in nums1:
        freq[num] = freq.get(num, 0) + 1

    for num in nums2:
        if freq.get(num, 0) > 0:
            res.append(num)
            freq[num] -= 1

    return res
