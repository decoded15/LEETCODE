'''

LeetCode 234: Palindrome Linked List
Approach: Fast & Slow Pointer + Reverse Second Half
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a singly linked list,
return True if the list is a palindrome,
otherwise return False.

Example:
Input: 1 -> 2 -> 2 -> 1
Output: True

Input: 1 -> 2 -> 3
Output: False

'''

def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        fast = head
        slow = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr :
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        first = head
        second = prev
        while second :
            if first.val != second.val :
                return False
            first = first.next
            second = second.next
        return True