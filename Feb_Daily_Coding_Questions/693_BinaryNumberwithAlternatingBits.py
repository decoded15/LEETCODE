'''
LeetCode 693: Binary Number with Alternating Bits
Approach: Bit-by-Bit Comparison using Right Shift
Time Complexity: O(1)  (At most 32 iterations)
Space Complexity: O(1)

Given a positive integer n, check whether its binary representation
contains alternating bits — meaning no two adjacent bits are the same.

The solution:
1. Extract the last bit using (n & 1).
2. Shift the number right.
3. Compare each current bit with the previous bit.
4. If two adjacent bits are equal, return False.
5. If no equal adjacent bits are found, return True.

Example:
Input: n = 5
Binary: 101
Output: True

Input: n = 7
Binary: 111
Output: False
'''

def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = n & 1  
        n >>= 1       

        while n:
            curr = n & 1

            if curr == prev:
                return False

            prev = curr
            n >>= 1

        return True