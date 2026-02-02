'''

LeetCode 2: Add Two Numbers
Approach: Linked List Traversal with Carry
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Key Idea:
- Traverse both lists simultaneously
- Add digits with carry
- Use a dummy node to build the result list cleanly

'''

def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        p1, p2 = l1, l2

        while p1 or p2 or carry:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0

            total = x + y + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dummy.next