'''
LeetCode 232: Implement Queue using Stacks
Approach: Two Stacks (Lazy Transfer Technique)
Time Complexity: Amortized O(1)
Space Complexity: O(n)

Implement a queue using two stacks.
One stack is used for enqueue (push) operations and the other for dequeue (pop/peek).

Elements are transferred from the input stack to the output stack only when needed,
which ensures efficient amortized performance.

Example:
push(1), push(2), pop() -> 1, peek() -> 2
'''

class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack