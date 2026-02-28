'''
LeetCode: Evaluate Reverse Polish Notation
Approach: Stack
Time Complexity: O(n)
Space Complexity: O(n)

Given an array of strings tokens representing an expression
in Reverse Polish Notation (Postfix notation).

Use a stack:
- If the token is a number, push it onto the stack.
- If the token is an operator (+, -, *, /),
  pop the top two elements, apply the operation,
  and push the result back onto the stack.

Division truncates toward zero.

Return the final value remaining in the stack.
'''

def evalRPN(tokens):
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