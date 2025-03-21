# https://leetcode.com/problems/add-digits/

" ** Follow up: Could you do it without any loop/recursion in O(1) runtime? **"
"""
    Brute Force:
        Time Complexity:  O(log n)
        Space Complexity: O(1)
"""
def bruteForce(num: int) -> int:  
    # Edge case: If num is 0, return 0 immediately.
    if num == 0:
        return 0  
    
    summation = 0

    # Extract digits and compute their sum iteratively.
    while num != 0:
        # Add the last digit to summation.
        summation += (num % 10)
        # Remove the last digit from num.
        num //= 10
    
    # If the sum is a multiple of 9, return 9; otherwise, return sum % 9.
    return 9 if summation % 9 == 0 else summation % 9



"""
    Optimal: Using mathematical formula
        Time Complexity:  O(1)
        Space Complexity: O(1)
    
    Formula: ** number % 9 **
            Edge case: if number == 0 then 0
                       if number % 9 == 0 then 9
"""
def optimal(num: int) -> int:  
    return 0 if num == 0 else 9 if num % 9 == 0 else num % 9 


# Main function
def addDigits(num: int) -> int:
    print(bruteForce(num))
    print(optimal(num))

addDigits(0)       # 0
addDigits(38)      # 2 (3 + 8) = 11 -> (1 + 1) = 2
addDigits(111)     # 3 (1 + 1 + 1) = 3
addDigits(9999)    # 9 (9 + 9 + 9 + 9) = 36 -> (3 + 6) = 9


