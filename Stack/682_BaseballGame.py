'''

LeetCode 682: Baseball Game
Approach: Stack
Time Complexity: O(n)
Space Complexity: O(n)

You are given a list of operations representing scores in a baseball game.
Operations include adding scores, removing scores, doubling scores,
and adding the last two scores.

Return the total sum of the scores.

'''

def calPoints(operations):
        stack = []
        for op in operations:
            if op == '+' :
                stack.append(stack[-1] + stack[-2])
            elif op == 'D' :
                stack.append(stack[-1] * 2)
            elif op == 'C' :
                stack.pop()
            else :
                stack.append(int(op))
        
        return sum(stack)