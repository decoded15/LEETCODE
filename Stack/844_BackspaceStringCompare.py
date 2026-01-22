'''

LeetCode 844: Backspace String Compare
Approach: Stack
Time Complexity: O(n)
Space Complexity: O(n)

Given two strings s and t, return True if they are equal
when both are typed into empty text editors.
'#' means a backspace character.

'''

def backspaceCompare(s, t):
        def process(st):
            stack = []
            for ch in st:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack

        return process(s) == process(t)