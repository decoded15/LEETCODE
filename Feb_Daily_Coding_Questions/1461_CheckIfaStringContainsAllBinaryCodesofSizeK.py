'''
1461. Check If a String Contains All Binary Codes of Size K
Difficulty: Medium
Topic: String, Sliding Window, HashSet

Problem:
Given a binary string s and an integer k,
return True if every possible binary code of length k
exists as a substring of s.
Otherwise, return False.

Key Insight:
• Total possible binary codes of length k = 2^k
• Use a sliding window of size k
• Store each substring of length k in a set
• If size of set == 2^k → return True

Approach:
1. Iterate from i = 0 to len(s) - k
2. Extract substring s[i:i+k]
3. Add to a set
4. Check if len(set) == 2**k

Time Complexity: O(n)
Space Complexity: O(2^k)

'''

def hasAllCodes(s, k):
        if len(s) < k:
            return False
        
        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
        
        return len(seen) == 2**k