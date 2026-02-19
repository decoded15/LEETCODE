'''
LeetCode 58: Length of Last Word
Approach: String Split
Time Complexity: O(n)
Space Complexity: O(n)

Given a string s consisting of words and spaces,
return the length of the last word in the string.

A word is defined as a maximal substring consisting
of non-space characters only.

The solution:
1. Split the string using whitespace.
2. Take the last word from the list.
3. Return its length.

Example:
Input:  "Hello World"
Output: 5

Input:  "   fly me   to   the moon  "
Output: 4
'''

def lengthOfLastWord(s):
        l = s.split()
        return len(l[-1])