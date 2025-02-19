# Sum of N numbers using Recursion

# -------- SUM --------
# With parameter to keep track of Sum
def sum_of_numbers (n: int, sum: int = 0):
    if (n < 1):
        print("Sum (i): %d" %sum)
        return
    
    sum_of_numbers(n-1, sum+n) 
sum_of_numbers(5)

# Without parameter 
def sum_of_nums (n) -> int:
    if (n < 1):
        return 0
    
    return (n + sum_of_nums(n - 1))

print("Sum (ii): %d" %sum_of_nums(10))

# ------- MULTI -------
def multi_of_nums (n: int) -> int:
    if (n < 1):
        return 1
    return (n * multi_of_nums(n - 1))

print("Multi : %d" %multi_of_nums(4))


"""
    Sum
    n = 3
    1 + 2 + 3 = 6
    ---------
    n = 5
    1 + 2 + 3 + 4 + 5 = 15
"""