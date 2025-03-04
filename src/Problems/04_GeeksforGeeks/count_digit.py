# https://www.geeksforgeeks.org/problems/count-digits5716/1


def evenlyDivides (n: int) -> int:
    ans = 0
    # Store `n` in a temporary variable to preserve its original value
    temp: int = n
    while (temp > 0):
        # Extract the last digit
        digit: int = temp % 10
        # If digit it not zero and `n` is divisible by digit then count++ (ans)
        if digit != 0 and n % digit == 0:
            ans += 1
        temp //= 10
    
    return ans

print("Answer: %d" %(evenlyDivides(12)))

"""
    ---------
    Example 1:
        Input: n = 12
        Output: 2
        Explanation: 1, 2 when both divide 12 leaves remainder 0.
    ---------
    Example 2:
        Input: n = 2446
        Output: 1
        Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.
            2446 / 1 = 2446  (✅)
            2446 / 2 = 1223  (✅)
            2446 / 4 = 611.5 (❌)
            2446 / 6 = 407.6 (❌)
    ---------
"""