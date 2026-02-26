'''
LeetCode 1356 — Sort Integers by The Number of 1 Bits

Problem:
Given an integer array arr, sort the integers by the number of 1's
in their binary representation. If two numbers have the same number
of 1 bits, sort them in ascending numerical order.

Approach:
1. For each number, convert it to binary using bin().
2. Count the number of '1's using count('1').
3. Store tuples in the form (ones_count, number).
4. Sort the tuple list — Python automatically sorts by first element,
   and then by second element if ties occur.
5. Extract the numbers from the sorted tuples to form the result.

Time Complexity: O(n log n)
Space Complexity: O(n)
'''

def sortByBits(arr):
        temp = [] 

        for i in arr:
            binary = bin(i)             
            ones = binary.count('1')   
            temp.append((ones, i))     

        temp.sort() 

        result = []
        for t in temp:
            result.append(t[1])   

        return result