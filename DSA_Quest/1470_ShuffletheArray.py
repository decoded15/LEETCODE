'''
LeetCode 1470: Shuffle the Array
Approach: Interleaving Two Halves
Time Complexity: O(n)
Space Complexity: O(n)

Given the array nums consisting of 2n elements in the form:
[x1, x2, ..., xn, y1, y2, ..., yn]

Return the array in the form:
[x1, y1, x2, y2, ..., xn, yn].

The solution:
1. Iterate from 0 to n-1.
2. For each index i:
   - Append nums[i]      (xi)
   - Append nums[i + n]  (yi)
3. Return the new shuffled array.

Example:
Input:  nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]

Explanation:
First half  = [2,5,1]
Second half = [3,4,7]
Interleaved = [2,3,5,4,1,7]
'''

def shuffle(nums, n):
        ans = []

        for i in range(n):
            ans.append(nums[i])      
            ans.append(nums[i+n])    

        return ans