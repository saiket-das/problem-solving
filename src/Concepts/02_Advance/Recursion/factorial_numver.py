# https://www.geeksforgeeks.org/problems/print-gfg-n-times/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-gfg-n-times


def factorialNumbers(n):
    if (n == 1):
        return 1
    
    return n * factorialNumbers(n - 1)
    
print(factorialNumbers(6))

"""
   6 .
   5
   4
   3 .
   2 .
   1 .
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