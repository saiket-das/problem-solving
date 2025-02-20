from collections import defaultdict

# https://leetcode.com/problems/integer-to-roman/


# Time Complexity: O(1) and Space COomplexity: O(1)
def intToRoman(num: int) -> str:
    # Define a list of tuples mapping integer values to their corresponding Roman numeral symbols.
    int_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'), (10, 'X'),  (9, 'IX'),  (5, 'V'),  (4, 'IV'), (1, 'I'),   
    ]

    # Initialize an empty string to store the resulting Roman numeral
    result: str = ""
    for value, roman in int_to_roman:     # O(13) -> O(1)
        # While the Current value is Less than or Equal to the Input number 
        while value <= num:    # TC -> O(3) -> O(1) as (1 <= num <= 3999)
            # Subtract the Current value from the Input number 
            # And Append the corresponding Roman numeral to the Result String.
            num -= value
            result += roman
        
    return result

print(intToRoman(40))



"""
    Example 1:
        Input: num = 3749
        Output: 'MMMDCCXLIX'
        Explanation:
            3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
             700 = DCC as 500 (D) + 100 (C) + 100 (C)
              40 = XL as 10 (X) less of 50 (L)
               9 = IX as 1 (I) less of 10 (X)
        Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
    --------------
    Example 2:
        Input: num = 58
        Output: 'LVIII'
        Explanation:
            50 = L
             8 = VIII
    --------------
    Example 3:
        Input: num = 1994
        Output: 'MCMXCIV'
        Explanation:
            1000 = M
             900 = CM
              90 = XC
               4 = IV
"""

