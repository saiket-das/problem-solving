# https://leetcode.com/problems/ugly-number/description/



"""
    Time Complexity:  O(log n)
    Space Complexity: O(1)
"""

def isUgly(n: int) -> bool:
    # Ugly numbers must be positive
    if (n < 1):
        return False
    
    # Repeatedly divide n by 2, 3, or 5 while possible
    for factor in [2, 3, 4, 5]:
        # Divide `n` by the factor until it's no longer divisible
        while (n % factor == 0):
            # Divide by the factor
            n /= factor
    
    # If n is reduced to 1, it's an ugly number
    return n == 1


print(isUgly(8))

""" 
    ----------------------------
    8 is Ugly number
      - 8 / 2 = 4
      - 8 / 2 = 2
      - 2 / 2 = 1 (return True)
    ----------------------------
    26 is not Ugly number
      - if (n % 2) == 0 then n = n / 2 -> n = 13
      - if (n = 13) (return False)
    ----------------------------
"""


"""
    ** An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5. **
    ----------
    Example 1:
        Input: n = 6
        Output: true
        Explanation: 6 = 2 * 3
    ----------
    Example 2:
        Input: n = 1
        Output: true
        Explanation: 1 has no prime factors.
    ----------
    Example 3:
        Input: n = 14
        Output: false
        Explanation: 14 is not ugly since it includes the prime factor 7.
    ----------
"""
