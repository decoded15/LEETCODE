'''
LeetCode 14: Longest Common Prefix
Approach: Horizontal Scanning
Time Complexity: O(n * m)
Space Complexity: O(1)

Given an array of strings, find the longest common prefix
shared among all the strings.

Start with the first string as the prefix.
Iteratively compare it with the next strings and shorten
the prefix until it matches the beginning of each string.

If at any point the prefix becomes empty,
there is no common prefix.
'''

def longestCommonPrefix(strs):
        prefix = strs[0]
        
        for s in strs:
            
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                
                if prefix == "":
                    return ""
        
        return prefix