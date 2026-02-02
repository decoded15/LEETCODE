'''

LeetCode 1544: Make The String Great
Approach: Stack (Adjacent Character Cancellation)
Time Complexity: O(n)
Space Complexity: O(n)

Given a string s consisting of lowercase and uppercase letters, the string is
considered "bad" if it contains two adjacent characters such that:
- They are the same letter
- One is lowercase and the other is uppercase

To make the string good, remove such adjacent pairs repeatedly until no more
bad pairs exist. Return the final string.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"

Example 2:
Input: s = "abBAcC"
Output: ""

'''

def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s :
            if stack and ch.isupper() and stack[-1] == ch.lower():
                stack.pop()
            elif stack and stack[-1].isupper() and ch == stack[-1].lower() :
                stack.pop()
            else :
                stack.append(ch)
        if stack :
            return "".join(stack)
        else :
            return ""