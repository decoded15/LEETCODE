'''
LeetCode 762: Prime Number of Set Bits in Binary Representation
Approach: Brute Force + Bit Counting + Prime Check
Time Complexity: O(n * log n)   (for each number, counting set bits)
Space Complexity: O(1)

Given two integers left and right, return the count of numbers in the
inclusive range [left, right] that have a prime number of set bits
(1s in their binary representation).

The solution:
1. Iterate from left to right.
2. For each number:
   - Count the number of set bits using bin(num).count('1').
   - Check if the count is a prime number.
3. Increment the answer if it is prime.
4. Return the total count.

Example:
Input: left = 6, right = 10
Binary representations:
6  -> 110  (2 set bits, prime)
7  -> 111  (3 set bits, prime)
8  -> 1000 (1 set bit, not prime)
9  -> 1001 (2 set bits, prime)
10 -> 1010 (2 set bits, prime)

Output: 4
''' 

def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def is_prime(num):
            c = 0
            for i in range(1, num + 1):
                if num % i == 0 :
                    c += 1
            if c == 2:
                return True
            else :
                return False
        count = 0
        for num in range(left, right + 1):
            bits = bin(num).count('1')
            if is_prime(bits):
                count += 1
        return count
