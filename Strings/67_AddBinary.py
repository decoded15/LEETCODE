'''
LeetCode 67: Add Binary
Approach: Right-to-Left Binary Addition with Carry
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))

Given two binary strings a and b, return their sum as a binary string.

The solution simulates manual binary addition:
1. Start from the last characters of both strings.
2. Add corresponding bits along with carry.
3. Append (total % 2) to result.
4. Update carry as (total // 2).
5. Continue until both strings and carry are exhausted.

Example:
Input: a = "1010", b = "1011"
Output: "10101"
'''

def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(result[::-1])