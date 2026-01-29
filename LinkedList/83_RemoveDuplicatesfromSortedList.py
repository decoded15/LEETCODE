'''

LeetCode 83: Remove Duplicates from Sorted List
Approach: Single Pointer Traversal
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a sorted linked list,
delete all duplicates such that each element
appears only once.

Example:
Input:  1 -> 1 -> 2 -> 3 -> 3
Output: 1 -> 2 -> 3

'''

def deleteDuplicates(head):
        curr = head
        while curr and curr.next :
            if curr.val == curr.next.val :
                curr.next = curr.next.next
            else :
                curr = curr.next
        return head