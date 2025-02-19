# https://leetcode.com/problems/fibonacci-number/description/


"""
    :type n: int
    :rtype: int
"""
# Time Complexity: O(2^n) -> (Exponential TC)
def fib (n) -> int:
    if (n <= 1):
        return n    # 0 or 1
    
    return fib(n-1) + fib(n-2)

print(fib(10))


"""
    # f(n) = f(n-1) + f(n-2)
    ------------
    Example 1:
        Input: n = 2
        Output: 1
        Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
    ------------
    Example 2:    
        Input: n = 3
        Output: 2
        Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
    ------------
    Example 3:
        Input: n = 4
        Output: 3
        Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
    ------------
"""
