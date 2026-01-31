'''

LeetCode 203: Remove Linked List Elements
Approach: Single Traversal with Dummy Node
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a linked list and an integer val,
remove all the nodes of the linked list that have Node.val == val,
and return the new head.

'''

def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next :
            if curr.next.val == val :
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next