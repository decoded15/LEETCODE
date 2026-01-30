'''

LeetCode 160: Intersection of Two Linked Lists
Approach: Two Pointer Traversal with Pointer Redirection
Time Complexity: O(n + m)
Space Complexity: O(1)

Given the heads of two singly linked lists,
return the node at which the two lists intersect.
If the two linked lists do not intersect, return None.

Intersection is defined by reference, not by value.

'''

def getIntersectionNode(headA, headB):
        first = headA
        second = headB
        while first != second :
            if first :
                first = first.next
            else :
                first = headB
            
            if second :
                second = second.next
            else :
                second = headA
        
        return first