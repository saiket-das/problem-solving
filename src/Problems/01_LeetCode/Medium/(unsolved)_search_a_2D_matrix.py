# 

"""
    Time Complexity:  O(m + n)
    Space Complexity: O(1)
"""

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
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

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11))


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