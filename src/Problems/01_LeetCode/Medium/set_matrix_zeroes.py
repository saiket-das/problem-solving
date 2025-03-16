# https://leetcode.com/problems/set-matrix-zeroes/description/


"""
    Brute Force:
        Time Complexity:  O((n * m) + (n + m)) + O(n * m)
        Space Complexity: O(1)
"""
def mark_row(matrix, row_index, num_cols):
    # Marks all non-zero elements in the given row as -1
    for col in range(num_cols):
        if matrix[row_index][col] != 0:
            matrix[row_index][col] = -1
        
def mark_col(matrix, col_index, num_rows):
    # Marks all non-zero elements in the given column as -1
    for row in range(num_rows):
        if matrix[row][col_index] != 0:
            matrix[row][col_index] = -1

def brute_force(matrix: list[list[int]]) -> None:
    row_len = len(matrix)
    col_len = len(matrix[0])

    # Mark rows and columns that should be set to zero
    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] == 0:
                mark_row(matrix, row, col_len)
                mark_col(matrix, col, row_len)
    
    # Replace flagged (-1) elements with zero
    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] == -1:
                matrix[row][col] = 0

    return matrix


"""
    Better:
        Time Complexity:  O(n * m) + O(n * m)
        Space Complexity: O(n) + O(m)
"""
def better(matrix: list[list[int]]) -> None:
    # Get the dimensions of the matrix
    n = len(matrix)
    m = len(matrix[0])

    # Arrays to track which rows and columns should be set to zero
    row_flags = [0] * n     # Stores which rows should be zeroed
    col_flags = [0] * m     # Stores which columns should be zeroed

    # Identify rows and columns that need to be set to zero
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row_flags[i] = 1    # Mark row to be zeroed
                col_flags[j] = 1    # Mark column to be zeroed
    
    for i in range(n):
        for j in range(m):
            if row_flags[i] == 1 or col_flags[j] == 1:
                matrix[i][j] = 0    # Set element to zero
        
    return matrix


"""
    Optimal:
        Time Complexity:  O(n * m) + O(n * m)
        Space Complexity: O(1)
"""
def optimal(matrix: list[list[int]]) -> None:
    # Get the dimensions of the matrix
    n = len(matrix)
    m = len(matrix[0])

    # Flag to track if the first column needs to be zeroed
    col_0 = 1
    
    # Step 1: Use First Row and Column as Markers
    # Iterate through the matrix to mark rows and columns that should be zeroed
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # Mark the first cell of the row
                matrix[i][0] = 0

                # Mark the first cell of the column (only if it's not the first column)
                if j != 0:
                    matrix[0][j] = 0
                # If the zero is in the first column, mark `col_0` as 0
                else:
                    col_0 = 0
    
    # Step 2: Update Inner Cells Based on Markers
    # Skip the first row and first column for now
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0:
                # If either the row marker or column marker is 0, set this cell to 0
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
    
    # Step 3: Zero Out the First Row If Needed
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    
    # Step 4: Zero Out the First Column If Neede
    if col_0 == 0:
        for i in range(n):
            matrix[i][0] = 0
    
    return matrix 


# Main Function
def setZeroes(matrix: list[list[int]]) -> None:
    # print(brute_force(matrix))
    # print(better(matrix))
    print(optimal(matrix))


setZeroes([[-1],[2],[3]])                                     # [[-1],[2],[3]]
setZeroes([[1,1,1],[1,0,1],[1,1,1]])                          # [[1,0,1],[0,0,0],[1,0,1]]
setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])                    # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]])    # [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


"""
    Optimal Approach: 
        Step 1: Identify Which Rows and Columns Should Be Zeroed
            - Iterate through the matrix.
            - When encountering a 0 at matrix[i][j]:
              • Mark its row by setting matrix[i][0] = 0.
              • Mark its column by setting matrix[0][j] = 0 (if j != 0).
              • If the 0 is in the first column, track it separately using col_0 = 0.
              
            Example After Step 1: For input:
                [
                  [1, 2, 3],
                  [4, 0, 6],
                  [7, 8, 9]
                ]
            After marking:
                [
                  [1, 0, 3],  # Column 1 marked in first row
                  [0, 0, 6],  # Row 1 marked in first column
                  [7, 8, 9]
                ]
        
        Step 2: Zero Out Cells Based on Markers
            - Iterate excluding the first row and first column.
            - If either matrix[0][j] == 0 (column is marked) OR matrix[i][0] == 0 (row is marked),
              • Set matrix[i][j] = 0.
            Example After Step 2:
            [
              [1, 0, 3],  
              [0, 0, 0],  # Entire row zeroed
              [7, 0, 9]  # Column 1 zeroed
            ]
        
        Step 3: Zero Out the First Row If Needed
            - If the top-left corner (matrix[0][0]) is 0, set the entire first row to 0.
        
        Step 4: Zero Out the First Column If Needed
            - If col_0 == 0, set the entire first column to 0.
"""