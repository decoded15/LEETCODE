'''
LeetCode 485: Max Consecutive Ones
Approach: Linear Scan with Counter
Time Complexity: O(n)
Space Complexity: O(1)

Given a binary array nums, return the maximum number of consecutive 1's in the array.

The solution:
1. Traverse the array once.
2. Maintain a current_count to track consecutive 1s.
3. Update max_count whenever current_count increases.
4. Reset current_count to 0 when a 0 is encountered.

Example:
Input:  [1,1,0,1,1,1]
Output: 3

Explanation:
The first two 1s give a streak of 2.
After encountering 0, the streak resets.
The last three 1s give a streak of 3, which is the maximum.
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        
        return max_count