'''
LeetCode 868 - Binary Gap

🔹 Problem:
Given a positive integer n, return the longest distance between any two adjacent 1's 
in the binary representation of n. If there are no two adjacent 1's, return 0.

🔹 Approach:
1. Convert the number to binary using bin(n)[2:].
2. Traverse the binary string.
3. Track the index of the previous '1'.
4. Whenever we encounter another '1', calculate the distance:
       gap = current_index - previous_index
5. Keep updating the maximum gap.
6. Return the maximum gap.

🔹 Key Idea:
We only care about positions of '1's and measure the distance between consecutive ones.

🔹 Time Complexity:
O(k) — where k is the number of bits in n.

🔹 Space Complexity:
O(1)

🔹 Example:
Input: 22
Binary: 10110
Positions of 1s: 0, 2, 3
Gaps: 2 and 1
Output: 2
'''

def binaryGap(n):
        b = bin(n)[2:]   
        
        max_gap = 0
        prev_index = -1
        
        for i in range(len(b)):
            
            if b[i] == '1':
                
                if prev_index != -1:
                    gap = i - prev_index
                    if gap > max_gap:
                        max_gap = gap
                
                prev_index = i
        
        return max_gap