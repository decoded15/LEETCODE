'''
LeetCode 70: Climbing Stairs
Approach: Iterative Dynamic Programming (Fibonacci Pattern)
Time Complexity: O(n)
Space Complexity: O(1)

You are climbing a staircase with n steps.
Each time you can either climb 1 step or 2 steps.

The number of ways to reach step n follows the relation:
ways(n) = ways(n-1) + ways(n-2)

This is equivalent to the Fibonacci sequence.
The solution iteratively computes the result using two variables
to maintain constant space.

Example:
Input: n = 3
Output: 3
'''

def climbStairs(n):
        if n <= 2:
            return n

        prev1 = 2
        prev2 = 1

        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1