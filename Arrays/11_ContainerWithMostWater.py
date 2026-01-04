'''

LeetCode 11: Container With Most Water
Approach: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are
(i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Example 2:
Input: height = [1,1]
Output: 1

'''
def maxArea(height):
        left = 0
        right = len(height) - 1
        maxarea = 0
        while(left < right):
            area = (right - left) * min(height[left], height[right])

            if area >  maxarea :
                maxarea = area

            if height[left] < height[right] :
                left+=1
            else :
                right -= 1
        return maxarea