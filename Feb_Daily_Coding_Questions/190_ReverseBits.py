'''
LeetCode 190: Reverse Bits
Approach: Bit-by-Bit Reversal using Shift Operators
Time Complexity: O(1)  (Always 32 iterations)
Space Complexity: O(1)

Reverse bits of a given 32-bit unsigned integer.

The solution:
1. Extract the last bit using (n & 1).
2. Shift the result left to make space.
3. Insert the extracted bit using OR.
4. Shift the original number right.
5. Repeat 32 times.

Example:
Input:  00000010100101000001111010011100
Output: 00111001011110000010100101000000
'''

def reverseBits(n):
        result = 0

        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        return result