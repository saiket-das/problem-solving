# Greatest Common Divisor (GCD) and Highest Common Factor (HCF)


def gcd_hcf (num1, num2) -> int:
    # Greatest Common Divisor
    gcd: int = 1
    # Find the min value from both number
    n: int = min(num1, num2)    # TC: O(1)

    # Approach 1 - TC: O(n) 
    # i: int = 1
    # while (i <= n):    # TC: O(n) -> (n is min value between Number 1 and 2)
    #     # If Number 1 and 2 both are divided by (i) and (i) else than (gdc) value then (gcd = i)
    #     if ((num1 % i == 0) and (num2 % i == 0) and (gcd < i)):
    #         gcd = i  
    #     i += 1
    
    # Approach 2 - TC: O(n) (Better in some cases - e.g. 20 and 40, in that case O(1))
    for i in range(n, 1, -1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            # If Number 1 and 2 both are divided by (i) and (i) else than (gdc) value then (gcd = i)
            gcd = i
            break
    return gcd


print(gcd_hcf(12, 9))


"""
    num1 = 9 and num2 = 12
        12 = {1, 2, 3, 4, 6, 12}
        9  = {1, 3, 9}

        GCD(9, 12) -> (1, 3) = 3
        HCD(9, 12) -> (1, 3) = 1 * 3 = 3
    
    -------------
    Solution:
        1. Initialize 'gcd' variable with default 0 value
        2. Find Max number ('n') between Number 1 and 2
        3. Loop through 1 to n
        4. If Number 1 and 2 both are divided by 'i' and 'i' else than 'gcd' value then 'gcd' = i
        5. Return 'gcd' value
"""

# Math solution - Time Complexity: O(logφ min(a, b))
def math_gcd (a: int , b: int) -> int:

    while (a > 0 and b > 0):
        if (a < b):
            b = b % a
        else:
            a = a % b
        
    return b if (a == 0) else a
    


print("Math GCD: %d" %(math_gcd(9, 12)))


"""
    GCD
    (a, b) = gcd (a - b, b)
        - gcd (20, 15) = gcd (5, 15)
        - gcd (15, 5)  = gcd (10, 5)
        - gcd (10, 5)  = gcd (5, 5)
        - gcd (5, 5)   = gcd (0, 5)

        When one of the value is 0 then another one is the answer
"""