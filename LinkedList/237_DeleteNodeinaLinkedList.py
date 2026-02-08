'''
LeetCode 237: Delete Node in a Linked List
Approach: Copy Next Node Value and Skip
Time Complexity: O(1)
Space Complexity: O(1)

You are given a node to delete in a singly linked list,
but you do not have access to the head of the list.

Since the previous node is unavailable, the solution copies
the value of the next node into the current node and bypasses
the next node.

Example:
Input: 4 -> 5 -> 1 -> 9, delete node = 5
Output: 4 -> 1 -> 9
'''

def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next