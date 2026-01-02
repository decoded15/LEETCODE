'''

LeetCode 125: Valid Palindrome
Approach: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)

Given a string s, return true if it is a palindrome, or false otherwise.

A string is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Alphanumeric characters include letters and numbers.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: s = "race a car"
Output: false

Example 3:
Input: s = " "
Output: true

'''

def Palindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

    return True

    