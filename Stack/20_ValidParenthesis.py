'''

LeetCode 20: Valid Parentheses
Approach: Stack (LIFO)
Time Complexity: O(n)
Space Complexity: O(n)

Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
- Open brackets are closed by the same type of brackets
- Open brackets are closed in the correct order
- Every closing bracket has a corresponding opening bracket

Example 1:
Input: s = "()"
Output: True

Example 2:
Input: s = "()[]{}"
Output: True

Example 3:
Input: s = "(]"
Output: False

'''

def isValid(s):
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in mapping:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack
