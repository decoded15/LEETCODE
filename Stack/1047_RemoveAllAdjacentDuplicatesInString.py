'''

LeetCode 1047: Remove All Adjacent Duplicates in String
Approach: Stack (LIFO)
Time Complexity: O(n)
Space Complexity: O(n)

You are given a string s consisting of lowercase English letters.
Repeatedly remove adjacent duplicate characters until no such
duplicates remain.

Example:
Input: s = "abbaca"
Output: "ca"

Explanation:
abbaca -> aaca -> ca

'''

def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if stack and stack[-1] == ch :
                stack.pop()
            else :
                stack.append(ch)
        return "".join(stack)