# 

"""
    Time Complexity:  O(m * n)
    Space Complexity: O(1)
"""
def bruteForce(matrix: list[list[int]], target: int) -> bool:
    # Get matrix dimensions
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == target:
                return True
    
    # Target not found
    return False



"""
    Better
        Time Complexity:  O(m + n)
        Space Complexity: O(1)
"""
def better(matrix: list[list[int]], target: int) -> bool:
    # Get matrix dimensions
    m, n = len(matrix), len(matrix[0])

    # Start from the top-right corner
    row, col = 0, n - 1

    while (row < m and col >= 0):
        # Target found
        if (matrix[row][col] == target):
            return True
        # Move left
        elif (matrix[row][col] > target):
            col -= 1
        # Move down
        else:
            row += 1
    
    # Target not found
    return False


"""
    Better
        Time Complexity:  O(m + n)
        Space Complexity: O(1)
"""
def optimal(matrix: list[list[int]], target: int) -> bool:
    # Get matrix dimensions
    m, n = len(matrix), len(matrix[0])

    # Treat the 2D matrix as a flattened 1D array for binary search
    low, high = 0, (n * m - 1)

    while low <= high:
        # Calculate the middle index of the virtual 1D array
        mid = (low + high) // 2
        # Convert the 1D index back to 2D matrix coordinates
        row, col = mid // n, mid % n

        # Check if the target is found
        if matrix[row][col] == target:
            return True
        
        # If the current element is less than the target, search the right half
        if matrix[row][col] < target:
            low = mid + 1
        # Otherwise, search the left half
        else:
            high = mid - 1
    
    # Target not found
    return False


# Main function
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # print(bruteForce(matrix, target))
    # print(better(matrix, target))
    print(optimal(matrix, target))


searchMatrix([[0,1,2,3],[4,5,6,7],[8,9,10,11]], 11)          # True
searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11)    # True
searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 61)    # False


"""
    [1,   3,  5,  7]
    [10, 11, 16, 20]
    [23, 30, 34, 60]
    
    Target: 3
"""
   
"""
    ** You must write a solution in O(log(m * n)) time complexity. **
    -----------
    Example 1:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        Output: true
    -----------
    Example 2:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
        Output: false
    -----------
"""