# https://leetcode.com/problems/search-a-2d-matrix-ii/description/



"""
    Brute Force: 
        TC: O(m * n)
        SC: O(1)
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
        TC: O(m * log n)
        SC: O(1)
"""
def better(matrix: list[list[int]], target: int) -> bool:
    # Get matrix dimensions
    m, n = len(matrix), len(matrix[0])

    # Binary search in current row 
    for i in range(n):
        # Set binary search boundaries for the current row
        low, high = 0, n - 1

        # Perform binary search within the current row
        while low <= high:
            mid = (low + high) // 2

            # Check if the target is found
            if matrix[i][mid] == target:
                return True
            
            # If target is greater, ignore the left half
            if matrix[i][mid] < target:
                low = mid + 1
            # If target is smaller, ignore the right half
            else:
                high = mid - 1
        
    # Target not found
    return False

        

"""
    Optimal
        TC: O(m + n)
        SC: O(1)
"""
def optimal(matrix: list[list[int]], target: int) -> bool:
    # Get matrix dimensions
    m, n = len(matrix), len(matrix[0])

    # Start from the top-right corner of the matrix
    row, col = 0, n - 1

    # Searching while within matrix bounds
    while row < m and col >= 0:
        # If the target is found, return True
        if matrix[row][col] == target:
            return True
        # If the current element is less than the target, move down
        elif matrix[row][col] < target:
            row += 1
        # If the current element is greater than the target, move left
        else:
            col -= 1
    
    # Target not found
    return False




# Main function
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # print(bruteForce(matrix, target))
    # print(better(matrix, target))
    print(optimal(matrix, target))


searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)     # True
searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)    # False


"""
    Target: 14
    [   
        L                H
        0    1   2   3   4
      0 [1,  4,  7,  11, 15]
      1 [2,  5,  8,  12, 19]
      2 [3,  6,  9,  16, 22]
      3 [10, 13, 14, 17, 24]
      4 [18, 21, 23, 26, 30]

        low = 0, high = 4
            matrix[low][high] > target:
                high -= 1

        low = 0, high = 3
            11 < 14:
                low += 1  

        low = 1, high = 3
            12 < 14:
                low += 1

        low = 2, high = 3
            16 > 14:
                high -= 1  
        
        low = 2, high = 2
            9 < 14:
                low += 1

        low = 3, high = 2
            14 == 14:
                return
    ]
"""