# https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1


sum: int = 0
def sumOfSeries (i):
    if (i < 1):    # Base Case
        return 0
    return (i**3 + sumOfSeries(i-1))
    
print(sumOfSeries(5))

"""
    Example 1:
        nput: n = 5
        Output: 225
        1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225
    ----------
    Example 2:
        Input: n = 
        Output: 784
        Explanation: 1^3 + 2^3 + 3^3 + 4^3 + 5^3 + 6^3 + 7^3 = 784
"""