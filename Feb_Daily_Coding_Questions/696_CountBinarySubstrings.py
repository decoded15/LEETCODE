'''
LeetCode 696: Count Binary Substrings
Approach: Consecutive Group Counting
Time Complexity: O(n)
Space Complexity: O(1)

Given a binary string s, return the number of non-empty substrings
that have the same number of 0's and 1's, and all the 0's and 1's
in those substrings are grouped consecutively.

The solution:
1. Traverse the string and count consecutive groups of identical characters.
2. Keep track of the previous group size and current group size.
3. Every time the character changes, add min(previous_group, current_group)
   to the result.
4. Add the final min(previous_group, current_group) after the loop ends.

Example:
Input:  "00110011"
Groups: 2, 2, 2, 2
Output: 6

Explanation:
Valid substrings are:
"0011", "01", "1100", "10", "0011", "01"
'''

def countBinarySubstrings(s):
        prev = 0     
        curr = 1      
        count = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                count += min(prev, curr)
                prev = curr
                curr = 1

        count += min(prev, curr)
        return count