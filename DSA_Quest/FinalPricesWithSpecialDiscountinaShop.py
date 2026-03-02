'''
LeetCode: Final Prices With a Special Discount in a Shop
Approach: Monotonic Stack (Next Smaller or Equal Element)
Time Complexity: O(n)
Space Complexity: O(n)

Given an array prices where prices[i] is the price of the ith item,
for each item find the first item to its right with price
less than or equal to it.

Use a monotonic increasing stack to track indices.
When a smaller or equal price is found, apply the discount
to the corresponding index stored in the stack.

Return the updated prices array.
'''

def finalPrices(prices):
        stack = [] 
        
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                prices[idx] -= prices[i]
            
            stack.append(i)
        
        return prices