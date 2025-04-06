# https://leetcode.com/problems/sqrtx/description/


"""
    Brute Force: Linear Search
       Time Complexity:  O(n/2) -> O(n)
       Space Complexity: O(1)
"""
def brute_force(x: int) -> int:    
    # Initialize the variable to store the largest integer whose square is ≤ x
    squared = 0

    # Iterate from 1 to x-1
    for i in range(1, x + 1):
        # Update squared to the current valid integer
        if i * i <= x:
            squared = i
        # If i^2 exceeds x, stop the loop
        else:
            break
        
    # Return the largest integer whose square is ≤ x
    return squared



"""
    Optimal: Binary Search
       Time Complexity:  O(log n)
       Space Complexity: O(1)
"""
def optimal(x: int) -> int:
    # If x is 0 or 1, return x directly since their square roots are themselves
    if x == 0 or x == 1:
        return x
    
    # Initialize two pointer
    low, high = 1, x

    # Initialize `squared` to store the largest integer whose square is ≤ x
    squared = 1
    
    while low <= high:
        # Calculate the middle point of the search range
        mid = (low + high) // 2
        
        # If mid squared is less than or equal to x, it's a valid value for the square root
        if mid * mid <= x:
            squared = mid     # Update `squared` to the current valid mid value
            low = mid + 1     # Narrow the search to the right half (higher values)
        else:
            high = mid - 1    # Narrow the search to the left half (lower values)
    
    return squared



# Main function
def mySqrt(x: int) -> int:
    # print(brute_force(x))
    print(optimal(x))

# mySqrt(8)              # 2
# mySqrt(9)              # 3
# mySqrt(24)             # 4
# mySqrt(35)             # 5
mySqrt(2147483647)     # 46340