'''

LeetCode 66: Plus One
Approach: Array Traversal with Carry Handling
Time Complexity: O(n)
Space Complexity: O(1)

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.

The digits are ordered from most significant to least significant.
Increment the integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]

Example 2:
Input: digits = [9]
Output: [1,0]

Example 3:
Input: digits = [9,9,9]
Output: [1,0,0,0]

'''

def plusOne(digits):
    n = len(digits)

    if digits[n - 1] < 9:
        digits[n - 1] += 1
        return digits

    i = n - 1
    while i >= 0 and digits[i] == 9:
        digits[i] = 0
        i -= 1

    if i == -1:
        digits.insert(0, 1)
    else:
        digits[i] += 1

    return digits
