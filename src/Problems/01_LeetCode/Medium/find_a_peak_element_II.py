# https://leetcode.com/problems/find-a-peak-element-ii/description/



"""
    Brute Force:
        TC: O(n * m)
        SC: O(1)

"""
def isPeakElement(matrix: list[list[int]], row: int, col: int, n: int, m: int) -> bool:
    current = matrix[row][col]
    
    # Check the value above, below, left, righht. If out of bounds, treat as -1
    top = matrix[row - 1][col] if row - 1 >= 0 else - 1
    down = matrix[row + 1][col] if row + 1 < n else - 1
    left = matrix[row][col - 1] if col - 1 >= 0 else - 1
    right = matrix[row][col + 1] if col + 1 < m else - 1
    
    # Return True only if current value is greater than all four neighbors
    return current > top and current > down and current > left and current > right
            

def bruteForce(matrix: list[list[int]]) -> list[int]:
    # Get matrix dimensions
    n, m = len(matrix), len(matrix[0])

    for row in range(n):
        for col in range(m):
            # Check if the current cell is a peak element
            if isPeakElement(matrix, row, col, n, m):
                return [row, col]    # Return the position of the first peak found
    
    # It will never execute
    return [-1, -1]




"""
    TC: O(n * log m)
    SC: O(1)
"""
def findMaxRowIndex(matrix: list[list[int]], n: int, m: int, col: int) -> list[int]:
    # Find the row index of the maximum element in the specified column
    maxValue, index = -1, -1

    for i in range(n):
        if maxValue < matrix[i][col]:
            maxValue = matrix[i][col]
            index = i
    
    return index


def optimal(matrix: list[list[int]]) -> list[int]:
    # Get matrix dimensions
    n, m = len(matrix), len(matrix[0])

    # Set binary search bounds for columns
    low, high = 0, m - 1

    while low <= high:
        # Find the middle column
        mid = (low + high) // 2

        # Get the row index of the maximum element in the middle column
        maxRowndex = findMaxRowIndex(matrix, n, m, mid)

        # Get the left neighbor (or -1 if out of bounds)
        left = matrix[maxRowndex][mid - 1] if mid - 1 >= 0 else -1
        # Get the right neighbor (or -1 if out of bounds)
        right = matrix[maxRowndex][mid + 1] if mid + 1 < m else -1

        # Check if the middle element is greater than both neighbors — it's a peak
        if left < matrix[maxRowndex][mid] and right < matrix[maxRowndex][mid]:
            return [maxRowndex, mid]
        # If the right neighbor is greater, move to the right half
        elif left < matrix[maxRowndex][mid]:
            low = mid + 1
        # Otherwise, move to the left half
        else:
            high = mid - 1
    
    # It will never execute
    return [-1, -1]


# Main function
def findPeakGrid(matrix: list[list[int]]) -> list[int]:
    # print(bruteForce(matrix))
    print(optimal(matrix))


findPeakGrid([[1,4],[3,2]])                        # [0,1] -> 4, 3 
findPeakGrid([[10,20,15],[21,30,14],[7,16,32]])    # [1,1] -> 30, 32