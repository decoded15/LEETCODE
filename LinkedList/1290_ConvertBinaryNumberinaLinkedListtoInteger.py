'''
LeetCode 1290: Convert Binary Number in a Linked List to Integer
Approach: Count Length + Binary to Decimal Conversion
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a singly linked list where each node contains a binary digit (0 or 1),
the linked list represents a binary number with the head as the most significant bit.

The solution first counts the number of nodes to determine bit positions,
then traverses the list again to compute the decimal value using powers of 2.

Example:
Input: 1 -> 0 -> 1
Output: 5
'''

class Solution(object):
    def getDecimalValue(self, head):
        temp = head
        res = 0
        count = 0
        current = head    
        while current is not None:
            count += 1
            current = current.next
        c = count - 1
        while temp :
            res += temp.val * (2 ** c)
            temp = temp.next
            c -= 1
        return res