# https://leetcode.com/problems/roman-to-integer/?envType=daily-question&envId=2025-02-10

"""
    :type s: str
    :rtype: int
"""
# Approach 1 
def romanToInt(s) -> int:
    ans = 0
    for i in range(len(s)):
        print(ans)
        # 1000
        if (s[i] == 'M'):
            if (i > 0 and (s[i-1] == "C")):
                ans += 900    # + 900, CM = 900
                ans -= 100    # - 100, Previous C value (100) which was the sum calculated earlier.
                continue
            ans += 1000
        # 500
        elif (s[i] == "D"):
            if (i > 0 and (s[i-1] == "C")):
                ans += 400    # + 400, CD = 400
                ans -= 100    # - 100, Previous C value (100) which was the sum calculated earlier.
                continue
            ans += 500
        # 100
        elif (s[i] == 'C'):
            if (i > 0 and (s[i-1] == "X")):
                ans += 90    # + 90, XC = 90
                ans -= 10    # - 10, Previous X value (10) which was the sum calculated earlier.
                continue
            ans += 100
        # 50
        elif (s[i] == "L"):
            if (i > 0 and (s[i-1] == "X")):
                ans += 40    # + 40, XL = 40
                ans -= 10    # - 10, Previous X value (10) which was the sum calculated earlier.
                continue
            ans += 50
        # 10
        elif (s[i] == 'X'):
            if (i > 0 and (s[i-1] == "I")):
                ans += 9    # + 9, IX = 9
                ans -= 1    # - 1, Previous I value (1) which was the sum calculated earlier.
                continue
            ans += 10
        # 5
        elif (s[i] == "V"):
            if (i > 0 and (s[i-1] == "I")):
                ans += 4    # + 4, IV = 4
                ans -= 1    # - 1, Previous I value (1) which was the sum calculated earlier.
                continue
            ans += 5
        # 1
        elif (s[i] == "I"):
            ans += 1
                           
    return ans

ans = romanToInt("LVIII")
print()
print("Answer: %s" %ans)
# MCMXCIV

#  -------------------------

# Approach 2
def romanToInt2(s) -> int:
    roman_to_int = { "I": 1, "V": 5,  "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

    ans = 0
    for char in s:
        ans += roman_to_int[char]

    return ans

ans = romanToInt2("MCMXCIV")
print()
print("Answer: %s" %ans)
# MCMXCIV
"""
    I = 1, IV = 4, IX = 10
    X = 10, XL = 40, XC = 90
    L = 50
    C = 100, CD = 400, CM = 900
    D = 500
    M = 1000
    -------------------------
    Example 1:
        Input: s = "III"
        Output: 3
        Explanation: III = 3.
    -------------------------
    Example 2:
        Input: s = "LVIII"
        Output: 58
        Explanation: L = 50, V = 5, III = 3.
    -------------------------
    Example 3:
        Input: s = "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    -------------------------
"""