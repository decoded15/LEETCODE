'''

LeetCode 122: Best Time to Buy and Sell Stock II
Approach: Greedy Profit Accumulation (Adjacent Price Comparison)
Time Complexity: O(n)
Space Complexity: O(1)

You are given an integer array prices where prices[i] is the price of a stock
on the ith day.

You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times),
but you must sell the stock before you buy again.

Return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0

'''


def maxProfit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit
