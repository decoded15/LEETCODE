'''

LeetCode 141: Linked List Cycle
Approach: Fast and Slow Pointers (Floyd’s Cycle Detection)
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a linked list, determine if the list contains a cycle.
A cycle exists if a node can be revisited while traversing the list.

'''

def hasCycle(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False