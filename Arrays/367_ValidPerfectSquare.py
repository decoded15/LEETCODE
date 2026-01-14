'''

LeetCode 367: Valid Perfect Square
Approach: Binary Search
Time Complexity: O(log n)
Space Complexity: O(1)

Given a positive integer num, return True if num is a perfect square,
otherwise return False.

You must not use any built-in square root function.

Example 1:
Input: num = 16
Output: True

Example 2:
Input: num = 14
Output: False

'''

def isPerfectSquare(num):
        low, high = 1, num

        while low <= high:
            mid = (low + high) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1

        return False