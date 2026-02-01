'''

LeetCode 150: Evaluate Reverse Polish Notation
Approach: Stack (Last-In-First-Out Evaluation)
Time Complexity: O(n)
Space Complexity: O(n)

You are given an array of strings tokens that represents an arithmetic
expression in Reverse Polish Notation.

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
Division between two integers truncates toward zero.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22

'''

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for ch in tokens:
            match ch:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    right, left = stack.pop(), stack.pop()
                    stack.append(left - right)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    right, left = stack.pop(), stack.pop()
                    stack.append(int(left / right))
                case _:
                    stack.append(int(ch))

        return stack[0]
        