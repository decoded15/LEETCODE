'''

LeetCode 3: Longest Substring Without Repeating Characters
Approach: Sliding Window with HashSet
Time Complexity: O(n)
Space Complexity: O(n)

Given a string s, find the length of the longest substring
without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3

Example 2:
Input: s = "bbbbb"
Output: 1

Example 3:
Input: s = "pwwkew"
Output: 3

'''
def lengthOfLongestSubstring(s):
        char_set = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len