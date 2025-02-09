# https://leetcode.com/problems/reverse-integer/

"""
    :type x: int
    :rtype: int
"""


def reverse(x):

    # If x == 0, there is not nothing to reverse. So, return 0
    if (x == 0):
        return 0
    
    reverse_num = 0
    temp = x
    temp = abs(temp)
    while (temp >= 1):
        digit = temp % 10
        reverse_num = (reverse_num * 10) + digit
        temp //= 10

    # If reversed number is less than 2^31 more than 2^31-1 then return 0
    INT_MIN = -2**31      # -2147483648
    INT_MAX = 2**31 - 1   # 2147483647
    if not (INT_MIN <= reverse_num <= INT_MAX):
        return 0

    if (x < 0):
       return (reverse_num * -1)
    else:
        return reverse_num


print(reverse(-2147483412))

# Edge case 
# -2147483412
# 1534236469

"""
    x = -321
    reverse_num = -1
    i.  digit (321 % 10) = 1
        reverse_num (0 * 10 + 1) = 1 
    ii. digit (32 % 10) = 2
        reverse_num (1 * 10 + 2) = 12 
    iii. digit (3 % 10) = 3
        reverse_num (12 * 10 + 3) = 123
"""