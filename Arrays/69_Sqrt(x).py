'''

LeetCode 69: Sqrt(x)
Approach: Binary Search on Answer Space
Time Complexity: O(log x)
Space Complexity: O(1)

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

You must not use any built-in exponent function or operator.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2

'''

def mySqrt(x) :
    if x < 2:
        return x

    low, high = 1, x
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
