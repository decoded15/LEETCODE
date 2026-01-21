'''

LeetCode 739: Daily Temperatures
Approach: Monotonic Decreasing Stack
Time Complexity: O(n)
Space Complexity: O(n)

Given an array of daily temperatures, return an array such that
for each day you know how many days you would have to wait until
a warmer temperature. If there is no future day for which this is
possible, put 0 instead.

Example:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

'''

def dailyTemperatures(temperatures):
        n = len(temperatures)
        res = [0] * n
        stack = []  

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index

            stack.append(i)

        return res