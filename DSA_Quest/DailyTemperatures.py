'''
LeetCode: Daily Temperatures
Approach: Monotonic Decreasing Stack (Next Greater Element)
Time Complexity: O(n)
Space Complexity: O(n)

Given an array temperatures, return an array answer such that
answer[i] is the number of days you must wait after the ith day
to get a warmer temperature.

Use a monotonic decreasing stack to store indices.
When a warmer temperature is found, pop indices from the stack
and compute the difference in indices to determine waiting days.

If no warmer day exists, value remains 0.
'''

def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        res = [0] * n
        stack = []  

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index

            stack.append(i)

        return res