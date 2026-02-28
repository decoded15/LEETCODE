'''
LeetCode: Exclusive Time of Functions
Approach: Stack + Previous Time Tracking
Time Complexity: O(n)
Space Complexity: O(n)

On a single-threaded CPU, functions are executed using a call stack.
Each log is formatted as: "function_id:start_or_end:timestamp".

Use a stack to simulate function calls.
Maintain a prev_time pointer to track the previous timestamp.

- When a function starts:
  If another function is running, update its exclusive time.
  Push the new function onto the stack.

- When a function ends:
  Pop it from the stack and update its time,
  including the end timestamp.
  Move prev_time forward.

Return the exclusive execution time of each function.
'''

def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        result = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            fid, typ, time = log.split(":")
            fid = int(fid)
            time = int(time)
            
            if typ == "start":
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
            
            else:  # "end"
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        
        return result
