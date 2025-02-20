# Prime numbers

# Brute Force - Time Complexity: O(n)
def primt_numbers (num) -> bool:

    # To keep track of total Divisor
    count: int = 0

    for i in range(1, num+1):
        primt_numbers(num % i)
        if (num % i == 0):
            count += 1
    
    # If Divisor (count) more than 2 then it's not Prime number
    return False if (count > 2) else True


# Better Approach - Time Complexity: O(√n) or O(sqrt(n))
def primt_numbers_2 (num) -> bool:
    # To keep track of total Divisor
    count: int = 0

    i: int = 1
    while (i * i <= num):
        if (num % i == 0):
            # Increment count by 2: one for the divisor 'i' and 
            # another for the corresponding pair 'num / i'
            count += 2
            
        i += 1    
    
    # If Divisor (count) more than 2 then it's not Prime number
    return False if (count > 2) else True


print(primt_numbers(9))      # Brute Force
print(primt_numbers_2(9))    # Better Approach


"""
    Rule of Prime number - Divisible by 1 and number by itself only (Total divisor: 2)

    Brute Force: TC - O(n)
        1. Initialize 'count" variable to keep track of all Divisor
        2. Loop though 1 to Number (Time Complexity: O(n))
        3. Check is the number divided by (i). If Yes then increment 'count'+ 1 (count++)
        4. If 'count' more then 2 then it is not a Prime number
    
    ----------------------------
    Better Approach: TC - O(n)
        n = 12
            1 * 12 = 12
            2 * 6  = 12
            3 * 4  = 12 
        
        1. Initialize count variable to keep track of all Divisor
        2. Loop though 1 to (√12 + 1) = 4
        3. Check is the number divided by (i). If Yes then increment count + 2(count += 2)
        4. If count more then 2 then it is not a Prime number
"""