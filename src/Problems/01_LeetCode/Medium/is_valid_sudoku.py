# https://leetcode.com/problems/valid-sudoku/description/

from collections import defaultdict

"""
    --------------------------
    Time Complexity:  0(9^2) => O(1)
    Space Complexity: O(1) -> (The space used by the hash maps (`rows`, `cols`, `squares`) is proportional to the size of the board.)
    -------------------------- 
    Thought Process:
        - Use three hash maps to track numbers in rows, columns, and 3x3 squares.
        - Rows: {0: {'1', '2', '3'}, 1: {'4', '5', '6'}, ...}
        - Columns: {0: {'8', '9'}, 1: {'6'}, ...}
        - Squares: {(0, 0): {'1', '2', '3', '8', '9'}, (1, 1): {'4', '5', '6'}, ...}
        - If a number is already present in the corresponding row, column, or square, the Sudoku is invalid.
    --------------------------
"""

def isValidSudoku(board: list[list[str]]) -> bool:
    # Hash maps to track numbers in rows, columns, and 3x3 squares
    rows: defaultdict[int, set] = defaultdict(set)
    cols: defaultdict[int, set] = defaultdict(set)
    squares: defaultdict[tuple, set]= defaultdict(set)    # key = (row/3, column/3) -> (0, 0), (0, 1).....(2, 2)

    # Iterate through each cell in the 9x9 board
    for r in  range(9):
        for c in range(9):
            if ((board[r][c]).isdigit()):
                # Check if the number is already in the current row, column, or square
                if ((board[r][c] in rows[r]) or 
                    (board[r][c] in cols[c]) or 
                    (board[r][c] in squares[r//3, c//3])):
                    return False    # Duplicate found, Sudoku is invalid
                
                # Add the number to the corresponding row, column, and square
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

    # No duplicates found, Sudoku is valid
    return True
                

print(isValidSudoku(
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","1",".",",",".",".","6","."]
    ,["9",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))


"""
    Sudoku Grid Representation with Rows, Columns, and Squares
    
    The Sudoku board is divided into 9 rows (R), 9 columns (C), and 9 squares (Sq).
    Each square is a 3x3 subgrid, identified by its top-left coordinate (row//3, column//3).

    Square Coordinates:
        - Squares are labeled as (row//3, column//3).
        - For example:
            - (0, 0): Top-left square (rows 0-2, columns 0-2)
            - (0, 1): Top-middle square (rows 0-2, columns 3-5)
            - (2, 2): Bottom-right square (rows 6-8, columns 6-8)

    Grid Visualization:    
                     Sqaure
      ---------------------------------                
      |   |   0    |   1     |    2   |
      |---|---------------------------|       
      | R |0  1  2 | 3  4  5 | 6  7  8|
      |-C-|---------------------------|
      | 0 |8  3  . | .  7  . | .  .  .|
    0 | 2 |6  .  . | 1  9  5 | .  .  .|
      | 2 |.  9  1 | .  .  . | .  6  .|
      |---|--------|---------|--------|
      | 3 |8  .  . | .  6  . | .  .  3|
    1 | 4 |4  .  . | 8  .  3 | .  .  1|
      | 5 |7  .  . | .  2  . | .  .  6|
      |---|--------|---------|--------|
      | 6 |.  6  . | .  .  . | 2  8  .|
    2 | 7 |.  .  . | 4  1  9 | .  .  5|
      | 8 |.  .  . | .  8  . | .  7  9|
       --------------------------------
"""

# Examples

"""
    -----------------------------------------------
    Example 1:
        Input: board = 
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    
        Output: true
    -----------------------------------------------
    Example 2:
        Input: board = 
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
        
        Output: false
        Explanation: 
            Same as Example 1, except with the 5 in the top left corner being modified to 8. 
            Since there are two 8's in the top left 3x3 sub-box, it is invalid
    -----------------------------------------------
"""