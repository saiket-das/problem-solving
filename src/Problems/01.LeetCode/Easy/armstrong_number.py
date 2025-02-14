# Armstrong Number

# Time Complexity: O(log10(n))
def armstrongNumber(n) -> bool:
    digits: list[int] = []
    count = 0
    temp = n

    while (temp != 0):
        digit: int = temp % 10
        temp //= 10
        count += 1
        digits.append(digit)

    ans: int = 0
    for digit in digits:
        ans += (digit**count)
        
    print(ans)
    return True if (n == ans) else False

print(armstrongNumber(1634))

"""
    What is Armstrong Number
    Example 1:
        n = 371
        3^3 + 7^3 + 1^3 = 371 --> (3 = Total digits)
        if (n == 371) return true
    
    Example 2:
        n = 1634
        1^4 + 6^4 + 3^4 + 4^4 = 1634 --> (4 = Total digits)
"""