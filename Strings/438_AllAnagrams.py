'''

LeetCode 438: Find All Anagrams in a String
Approach: Fixed-Size Sliding Window with Frequency Map
Time Complexity: O(n)
Space Complexity: O(1)

Given two strings s and p, return an array of all the start indices
of p's anagrams in s.

An anagram is a permutation of a string.
The order of output does not matter.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]

'''

class Solution:
    def findAnagrams(s, p):
        if len(p) > len(s):
            return []

        freq_p = {}
        freq_w = {}

        for ch in p:
            freq_p[ch] = freq_p.get(ch, 0) + 1

        window = len(p)

        for i in range(window):
            freq_w[s[i]] = freq_w.get(s[i], 0) + 1

        res = []
        if freq_w == freq_p:
            res.append(0)

        l = 0
        for r in range(window, len(s)):
            freq_w[s[r]] = freq_w.get(s[r], 0) + 1

            freq_w[s[l]] -= 1
            if freq_w[s[l]] == 0:
                del freq_w[s[l]]
            l += 1

            if freq_w == freq_p:
                res.append(l)

        return res
