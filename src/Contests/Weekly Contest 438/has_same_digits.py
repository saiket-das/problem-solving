# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/

"""
    Time Complexity:  O(n^2)
    Space Complexity: O(n)
"""
def hasSameDigits(s: str) -> bool:
    while (len(s) > 2):
        # New number after summing adjacent digits
        reduced_digits = []

        for i in range(len(s)-1):
            # Sum adjacent digits
            digit_sum = int(s[i]) + int(s[i+1])
            # Append only the last digit
            reduced_digits.append(str(digit_sum  % 10))
        
        # Update the number string `s` for the next iteration
        s = "".join(reduced_digits)
        
    # Check if the final two digits are the same
    return (s[0] == s[1])

print(hasSameDigits("3902"))


"""
    ** String concatenation (+=) in Python is slow because strings are immutable. **
    ------------

    Approach 1:
    while (len(s) > 2):
        # New number after summing adjacent digits
        reduced_str = ""        
        for i in range(len(s)-1):
            # Sum adjacent digits
            digit_sum = int(s[i]) + int(s[i+1])
            # Append only the last digit
            reduced_str += str(digit_sum  % 10)
      
        # Update the number for the next iteration
        s = reduced_str
      
    # Check if the final two digits are the same
    return (s[0] == s[1])
"""

"""
    -------------
    Example 1:
        Input: s = "3902"
        Output: true
        Explanation:
            Initially, s = "3902"
            First operation:
            (s[0] + s[1]) % 10 = (3 + 9) % 10 = 2
            (s[1] + s[2]) % 10 = (9 + 0) % 10 = 9
            (s[2] + s[3]) % 10 = (0 + 2) % 10 = 2
            s becomes "292"
            Second operation:
            (s[0] + s[1]) % 10 = (2 + 9) % 10 = 1
            (s[1] + s[2]) % 10 = (9 + 2) % 10 = 1
            s becomes "11"
            Since the digits in "11" are the same, the output is true.
    -------------
    Example 2:    
        Input: s = "34789"    
        Output: false    
        Explanation:
            Initially, s = "34789".
            After the first operation, s = "7157".
            After the second operation, s = "862".
            After the third operation, s = "48".
            Since '4' != '8', the output is false.
    -------------
"""
