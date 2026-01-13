'''

LeetCode 151: Reverse Words in a String
Approach: Split + Two-Pointer Reverse
Time Complexity: O(n)
Space Complexity: O(n)

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

The returned string should have:
- words in reverse order
- exactly one space between words
- no leading or trailing spaces

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"

'''

def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = 0
        w = s.split()
        r = len(w) - 1
        while l < r:
            w[l], w[r] = w[r], w[l]
            l += 1
            r -= 1
        return " ".join(w)