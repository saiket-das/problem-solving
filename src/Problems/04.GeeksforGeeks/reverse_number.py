# Reverse Number


def reverseNumber (n: int) -> int:
    reverse_num: int = 0

    temp: int = n
    while (temp != 0):
        digit: int = temp % 10
        temp //= 10
        reverse_num = (reverse_num * 10 + digit)
    
    #  Check is number in the range between (-2^31 and 2^31-1)
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    if not (INT_MIN <= reverse_num <= INT_MAX):
        return 0
    
    return (reverse_num * -1) if n < 0 else reverse_num


print(reverseNumber(1234))