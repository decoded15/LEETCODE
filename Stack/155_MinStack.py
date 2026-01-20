'''

LeetCode 155: Min Stack
Approach: Two Stacks (Main Stack + Min Stack)
Time Complexity: O(1) for all operations
Space Complexity: O(n)

Design a stack that supports push, pop, top,
and retrieving the minimum element in constant time.

'''

def __init__(self):
        self.stack = []
        self.min_stack = []

def push(self, val):
    """
    :type val: int
    :rtype: None
    """
    self.stack.append(val)

    if not self.min_stack:
        self.min_stack.append(val)
    else:
        self.min_stack.append(min(val, self.min_stack[-1]))

def pop(self):
    """
    :rtype: None
    """
    self.stack.pop()
    self.min_stack.pop()

def top(self):
    """
    :rtype: int
    """
    return self.stack[-1]

def getMin(self):
    """
    :rtype: int
    """
    return self.min_stack[-1]