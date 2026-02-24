'''
LeetCode: Set Mismatch
Approach: Hash Set + Mathematical Formula
Time Complexity: O(n)
Space Complexity: O(n)

Given an array nums containing numbers from 1 to n,
one number appears twice and one number is missing.

Use a set to detect the duplicate.
Use the formula n(n+1)/2 to compute expected sum.
Missing number = expected_sum - (actual_sum - duplicate).

Return [duplicate, missing].
'''

def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        s = set(nums)
        n = len(nums)
        
        for i in nums :
            if nums.count(i) > 1:
                res.append(i)
                break
        req_sum = (n * (n + 1))/2
        act_sum = sum(s)
        missing_num = req_sum - act_sum
        res.append(missing_num)
        return res