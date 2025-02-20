# https://www.geeksforgeeks.org/problems/print-gfg-n-times/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-gfg-n-times

# Time Complexity: O(n) and Space Complexity: O(n)
def factorialNumbers(n):
    if (n <= 1):
        return 1
    return n * factorialNumbers(n - 1)
    
def get_factorials_up_to_n(n, current: int = 1, result: list[int] = []):
    fact = factorialNumbers(current)
    if (fact> n):
        return result
    
    result.append(fact)
    return get_factorials_up_to_n(n, current + 1, result)

n = 3
result = get_factorials_up_to_n(n)
print(result)
"""
    Example 1:
        n = 3
        Factorial: 1 * 2 * 3 = 6
            1 < 6 ✅
            1 * 2 < 6 ✅
            1 * 2 * 3 < 6 ❌
        Output: 1 2
"""

"""
    Example 1:
        Input: n = 3
        Output: 1 2
        Explanation: The first factorial number is 1 which is less than equal to n. 
        The second number is 2 which is less than equal to n, 
        but the third factorial number is 6 which is greater than n. So we print only 1 and 2.
    
    ----------
    Example 2:
        Input: n = 6
        Output: 1 2 6
        Explanation: The first three factorial numbers are less than equal to n 
        but the fourth factorial number 24 is greater than n. So we print only first three factorial numbers

"""