# Recursion

def increment_recursion(num, stop):
    if (num > stop):    # Base Condition to stop the recursion function
        return 
    
    print(num, end = " ")
    increment_recursion(num + 1, stop)


increment_recursion(1, 10)    # 1 2 3 4 5 6 7 8 9 10
print()

# ------------------------

def triverse_recursion (n):
    if (n > 5):    # Base condition
        return n
    triverse_recursion(n + 1)
    print(n, end = " ")

triverse_recursion(1)
print()


"""
    Recursion
        1. Base Case
        2. Stack Overflow or Stack Space
        3. Recursive tree     
"""

