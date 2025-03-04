# https://leetcode.com/problems/pascals-triangle/description/



"""
    Time Complexity:  O(n^2)
    Space Complexity: O(n^2)
"""
def getRow(rowIndex: int) -> list[list[int]]:
    # Stores the rows of Pascal's Triangle
    pascal_triangle: list[list[int]] = [] 

    for row in range(rowIndex + 1):
        # Create a new row
        pascal_triangle.append([])

        for col in range(row + 1):
            # The first and last elements of each row are always 1
            if (col == 0 or row == col):
                pascal_triangle[row].append(1)
            else:
                # Each middle element is the sum of the two values above it
                value = pascal_triangle[row - 1][col - 1] + pascal_triangle[row - 1][col]
                pascal_triangle[row].append(value)
    
    return pascal_triangle[rowIndex]
        
print(getRow(3))


"""
    ----------
    Example 1:
        Input: numRows = 5
        Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    ----------
    Example 2:    
        Input: numRows = 1
        Output: [[1]]
    ----------
"""