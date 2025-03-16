# https://leetcode.com/problems/rotate-image/description/

"""
    Brute Force:
        Time Complexity:  O(n^2) + O(n^2)
        Space Complexity: O(n^2)
"""
def brute_force(matrix: list[list[int]]) -> None:
    # Get the dimensions of the matrix
    n = len(matrix)
    # Initialize an empty n x n matrix filled with zeros
    result = [[0] * n for _ in range(n)] 

    # Rotate the matrix 90 degrees clockwise
    # Iterate through Matrix
    for i in range(n):
        for j in range(n):    
            # Place element (i, j) from the original matrix 
            # into the rotated position (j, n - i - 1) in the new matrix
            result[j][n - i - 1] = matrix[i][j]
    
    # Copy values from 'result' back into 'matrix' to update it in place
    for i in range(n):
        for j in range(n):
            # Overwrite original matrix with rotated values
            matrix[i][j] = result[i][j]

    return matrix


"""
    Optimal: Transpose + Reverse
        Time Complexity:  O(n^2) + O(n)
        Space Complexity: O(1)
"""
def optimal(matrix: list[list[int]]) -> None:
    # Get the dimensions of the matrix
    n = len(matrix)

    # Transpose the matrix (swap elements across the diagonal)
    for row in range(n-1):
        for col in range(row + 1, n):
            # Swap only elements above the main diagonal to avoid redundant swaps
            if row != col:
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        # Reverse each row after transposition to achieve 90-degree rotation
        matrix[row].reverse()

    return matrix


# Main Function
def rotate(matrix: list[list[int]]) -> None:
    # brute_force(matrix)
    optimal(matrix)
    print(matrix)


rotate([[1,2,3],[4,5,6],[7,8,9]])                           # [[7,4,1],[8,5,2],[9,6,3]]
rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])    # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

"""
    Original
        [
          [1, 2, 3]
          [4, 5, 6]
          [7, 8, 9]
        ]
    After Rotate
        [
          [7, 4, 1]
          [8, 5, 2]
          [9, 6, 3]
        ]
                     --------            --------             --------
    i = 0, [0][0] -> `[0][2]`, [0][1] -> `[1][2]`, [0][2] -> `[2][2]`
    i = 1, [1][0] -> `[0][1]`, [1][1] -> `[1][1]`, [1][2] -> `[2][1]`
    i = 2, [2][0] -> `[0][0]`, [2][1] -> `[1][0]`, [1][2] -> `[1][0]`

"""

"""
    ** 
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
        DO NOT allocate another 2D matrix and do the rotation. 
    **
    ----------   
    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 100
    ----------
    Example 1
        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [[7,4,1],[8,5,2],[9,6,3]]
    ----------
    Example 2:    
        Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    ----------
"""