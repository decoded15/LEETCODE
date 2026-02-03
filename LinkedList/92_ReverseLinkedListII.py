'''
LeetCode 92: Reverse Linked List II
Approach: Dummy Node + Head Insertion (Partial Reversal)
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a singly linked list and two integers left and right,
reverse the nodes of the list from position left to position right
and return the modified list.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5, left = 2, right = 4
Output: 1 -> 4 -> 3 -> 2 -> 5
'''

def reverseBetween(head, left, right):
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next  
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next