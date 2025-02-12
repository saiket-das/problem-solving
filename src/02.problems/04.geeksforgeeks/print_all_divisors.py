import math

# Print all Divisors

def printAllDivisors(n) -> list[int]:
    divisors: list[int] = []
    # # Approce 1 (Brute force) -> Time Complexity: O(n)
    # for i in range(1, n+1):
    #     if (n % i == 0):
    #         divisors.append(i)
    # # ----------------------------

    # Approach 2 -> Time Complexity: O(√n + mlog(m)) -> (m = Size of List)
    # Time complexity: O(√n)
    i: int = 1 
    while (i*i <= n):    # TC: O(sqrt(n))
        if (n % i == 0):
            divisors.append(i)
            if not (n / i == i):
                divisors.append(n // i)
        i += 1

    # Sort before return
    divisors.sort()    # TC: O(mlog(m)) -> m is number of factors (means Size of List)
    return divisors

print(printAllDivisors(36))



"""
    n = 36
        1 * 36 = 36
        2 * 18 = 36
        3 * 12 = 36
        4 * 9  = 36
        6 * 6  = 36
    ❌ ------------- ❌
      | 9 * 4  = 36 |
      | 12 * 3 = 36 |
      | 18 * 2 = 36 |
      | 26 * 1 = 36 |
"""