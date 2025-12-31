'''

LeetCode 242: Valid Anagram
Approach: Hash Map (Frequency Count)
Time Complexity: O(n)
Space Complexity: O(n)

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t) :
            return False
        
        sf = {}
        tf = {}

        for ch in s:
            sf[ch] = sf.get(ch, 0) + 1
        
        for ch in t:
            tf[ch] = tf.get(ch, 0) + 1

        if sf == tf :
            return True
        else :
            return False