# https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-nth-root-of-m



"""
    Optimal: Binary Search
        Time Complexity:  O(log m * log n)
        Space Complexity: O(1)
"""
def optimal(n: int, m: int) -> int:
    # If m is 0 or 1, return m directly since their n-th root is themselves
    if m == 0 or m == 1:
        return m
    
    # Initialize two pointer
    low, high = 0, m

    # Perform binary search to find the integer part of the n-th root of m
    # TC: (log m)
    while low <= high:
        # Calculate the middle point of the search range
        mid = (low + high) // 2

        # If mid raised to the power of n is exactly equal to m, we've found the n-th root
        # TC: O(log n)
        if mid ** n == m:
            return mid
        
        # If mid raised to the power of n is greater than m, the n-th root must be smaller   
        elif mid ** n > m:
            high = mid - 1    # Narrow the search to the left half (lower values)

        # If mid raised to the power of n is less than m, the n-th root must be larger
        else:
            low = mid + 1     # Narrow the search to the right half (higher values)
    
    # If no exact n-th root is found, return -1 indicating no solution
    return -1

def nthRoot(n: int, m: int) -> int:
    print(optimal(n, m))


nthRoot(2, 9)     # 3  -> 3^2 = 9
nthRoot(3, 9)     # -1 -> 3rd root of 9 is not integer.
nthRoot(3, 27)
nthRoot(1, 14)
nthRoot(2, 14)