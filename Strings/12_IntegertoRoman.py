'''
LeetCode 12: Integer to Roman
Approach: Greedy (Value-Symbol Mapping)
Time Complexity: O(1)
Space Complexity: O(1)

Given an integer, convert it to its Roman numeral representation.

Roman numerals are formed by combining symbols representing
specific values. Some numbers use subtractive notation such as
4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD), and 900 (CM).

Use a greedy approach by mapping integer values to their
corresponding Roman symbols. Start from the largest value and
repeatedly append the symbol while subtracting the value from
the number until the number becomes zero.
'''

def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        res = ""
        
        for i in range(len(values)):
            
            while num >= values[i]:
                res += symbols[i]
                num -= values[i]
        
        return res