# https://leetcode.com/problems/palindrome-number/description/


"""
    :type x: int
    :rtype: bool
"""
def isPalindrome(x):
        # If x less than 0 than number can't be palindrome number
        if x < 0:
            return False; 
        
        temp = x
        answer = 0
        while (temp >= 1):
            # Extract digit from number and add into answer interger 
            digit = int(temp % 10)
            answer = (answer * 10) + digit
            temp /= 10
        
        return(answer == x)


print(isPalindrome(101))


"""
   x = 121
   intial Answer = 1
   
   i.   Digit (121 % 10) = 1
        Answer (0 * 10) + 1 = 1
   ii.  Digit (12 % 10) = 2
        Answer (1 * 10) + 2 = 12
   iii. Digit (1 % 10) = 1
        (12 * 10) + 2 = 121
"""