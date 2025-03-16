# https://leetcode.com/problems/pascals-triangle/description/


"""
    Time Complexity:  O(n^2)
    Space Complexity: O(n^2)
"""
def generate_pascal(numRows: int) -> list[list[int]]:
    # Stores the rows of Pascal's Triangle
    pascal_triangle: list[list[int]] = [] 

    for row in range(numRows):
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
    
    return pascal_triangle


"""
    Time Complexity:  O(n^2)
    Space Complexity: O(n^2)
"""
def generate_rows(numRows: int) -> list[list[int]]:
    # Initialize an empty list to store the rows of Pascal's Triangle
    pascal_triangle: list[list[int]] = []

    # Iterate through each row from 1 to numRows
    for row in range(1, numRows + 1):
        # Start each row with the first element as 1
        pascal_triangle.append([1])
        # Variable to store the computed value for each position in the row
        ans = 1

        # Compute the values for the current row using the binomial coefficient formula
        for col in range(1, row):
            # Multiply by (row - col) to calculate the next coefficient
            ans = ans * (row - col)
            # Divide by col to get the correct binomial coefficient
            ans = ans // (col)
            # Append the computed value to the row
            pascal_triangle[row - 1].append(ans)
    
    return pascal_triangle


# Find out the element at position (Row, Column)
def find_pascal_element(numRows: int, row: int) -> int:
    numRows = numRows - 1
    row = row - 1
    ans = 1
    
    for col in range(row):
        ans = ans * (numRows - col)
        ans = ans // (col + 1)

    return ans


# Main Function
def generate(numRows: int) -> list[list[int]]:
    # Approach 1
    # print(generate_pascal(numRows))

    # Approach 2
    print(generate_rows(numRows))

    # Find out the element at position (Row, Column)
    print(find_pascal_element(5, 3))    # 6
          
generate(5)


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