# https://leetcode.com/problems/find-missing-and-repeated-values/description/


from collections import defaultdict

"""
    Better: Hashing
        Time Complexity:  O(n^2) + O(n + n)
        Space Complexity: O(n + n)
"""
def better(grid: list[list[int]]) -> list[int]:
    # Get the size of the grid
    n = len(grid)
    size = n * n

    # Dictionary to count occurrences of each number in the grid
    freq_dict = defaultdict(int)

    # Count the occurrences of each number in the grid
    for i in range(n):
        for j in range(n):
            freq_dict[grid[i][j]] += 1
    

    duplicate_number, missing_number = -1, -1

    # Find duplicate and missing number
    for num in range(1, size + 2):
        if freq_dict[num] == 2:
            duplicate_number = num    # Number appears twice
        elif freq_dict[num] == 0: 
            missing_number = num      # Number is missing
        
        # If both values are found, exit early
        if duplicate_number != -1 and missing_number != -1:
            break
    
    return [duplicate_number, missing_number]


"""
    Better: Math
        Time Complexity:  O(n^2)
        Space Complexity: O(1)
"""
def optimal(grid: list[list[int]]) -> list[int]:
    # Get the size of the grid (assuming it's an n x n matrix)
    n = len(grid)
    
    actual_sum, actual_square_sum = 0, 0
    for i in range(n):
        for j in range(n):
            actual_sum += grid[i][j]
            actual_square_sum += (grid[i][j] ** 2)
    
    tota_n = n * n
    # Expected sum => Formula: (n * (n + 1) // 2)
    expected_sum = (tota_n * (tota_n + 1)) // 2
    i1 = actual_sum - expected_sum

    # Expected sum ^2 => Formula: (n *(n + 1) (2n + 1)) / 6
    expected_sqaure_sum = (tota_n * (tota_n + 1) * (2 * tota_n + 1)) // 6
    i2 = actual_square_sum - expected_sqaure_sum
    
    # Find (x + y = i3)
    i3 = i2 // i1

    ans = [None, None]
    ans[0] = (i1 + i3) // 2
    ans[1] = -(i1 - i3) // 2

    return ans


"""
    Time Complexity:  O(n^2) + O(n^2)
    Time Complexity:  O(n^2)
"""
def findMissingAndRepeatedValues(grid: list[list[int]]) -> list[int]:
    print(better(grid))
    # print(optimal(grid))


findMissingAndRepeatedValues([[1,3],[2,2]])                # [2, 4]
findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]])    # [9, 5]

"""
    ----------
    Example 1:
        Input: grid = [[1,3],[2,2]]
        Output: [2,4]
        Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
    ----------
    Example 2:    
        Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
        Output: [9,5]
        Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
    ----------
"""