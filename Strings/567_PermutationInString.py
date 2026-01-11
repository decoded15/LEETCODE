'''

LeetCode 567: Permutation in String
Approach: Fixed-Size Sliding Window with Frequency Map
Time Complexity: O(n)
Space Complexity: O(1)

Given two strings s1 and s2, return true if s2 contains
a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations
is a substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: True

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: False

'''
def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    freq1 = {}
    freq2 = {}

    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1

    window = len(s1)

    for i in range(window):
        freq2[s2[i]] = freq2.get(s2[i], 0) + 1

    if freq1 == freq2:
        return True

    l = 0
    for r in range(window, len(s2)):
        freq2[s2[r]] = freq2.get(s2[r], 0) + 1

        freq2[s2[l]] -= 1
        if freq2[s2[l]] == 0:
            del freq2[s2[l]]
        l += 1

        if freq1 == freq2:
            return True

    return False