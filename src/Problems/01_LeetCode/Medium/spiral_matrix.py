# https://leetcode.com/problems/spiral-matrix/description/

"""
    Time Complexity: O(n * m)
    Time Complexity: O(n * m)

    `n` = The number of Rows & `m` = The number of Columns
"""
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    # Get the number of rows and columns in the matrix
    row = len(matrix)
    col = len(matrix[0])
    
    # Define the boundaries for traversal
    top, bottom = 0, row - 1
    left, right = 0, col - 1

    # List to store the spiral order traversal
    result = []

    # Traverse the matrix in a spiral order
    while left <= right and top <= bottom:
        # Traverse from left to right along the top boundary
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1    # Move the top boundary down
    
        # Traverse from top to bottom along the right boundary
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1    # Move the right boundary left
    
        # Traverse from right to left along the bottom boundary (if not already traversed)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1    # Move the bottom boundary up
        
        # Traverse from bottom to top along the left boundary (if not already traversed)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1    # Move the left boundary right

    return result

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))             # [1,2,3,6,9,8,7,4,5]
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))    # [1,2,3,4,8,12,11,10,9,5,6,7]

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16], [17,18,19,20],[21,22,23,24]]))    


"""
    [
        L     R     
     T [1, 2, 3]
       [4, 5, 6]
       [7, 8, 9] B 
    ]
    ---------------

    [
        L           R
     T [1, 2,  3,   4]
       [5, 6,  7,   8]
       [9, 10, 11, 12] B
    ]
"""