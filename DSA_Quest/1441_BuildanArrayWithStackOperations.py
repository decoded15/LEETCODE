'''
LeetCode 1441: Build an Array With Stack Operations
Approach: Simulation (Greedy Stack Construction)
Time Complexity: O(n)
Space Complexity: O(n)

You are given:
- target → strictly increasing integer array
- n → stream of integers from 1 to n
- An empty stack
- Two operations: "Push" and "Pop"

Goal:
Return the list of stack operations required to build target
using numbers from 1 to n in order.

Rules:
1. Read numbers sequentially from 1 to n.
2. For every number read:
   - Perform "Push".
   - If the number is NOT in target at current position,
     immediately perform "Pop".
3. Stop once the stack equals target.

Core Idea:
- Maintain a pointer j for target.
- Iterate i from 1 to n.
- Always append "Push".
- If i == target[j], move j forward.
- Otherwise, append "Pop".
- Stop when all elements of target are processed.

Example:
Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
'''

def buildArray(target, n):
        result = []
        j = 0         
        for i in range(1, n + 1):         
            if j >= len(target):
                break            
            result.append("Push")           
            if i == target[j]:
                j += 1
            else:
                result.append("Pop")               
        return result