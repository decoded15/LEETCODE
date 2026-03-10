'''
LeetCode Problem: Maximum Depth of Binary Tree
Problem Number: 104
Difficulty: Easy

Approach:
Use recursion to compute the depth of the left and right subtrees.
The depth of the current node is 1 + max(left_depth, right_depth).

Time Complexity: O(n)
Space Complexity: O(h)

Where:
n = number of nodes
h = height of the tree
'''

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)