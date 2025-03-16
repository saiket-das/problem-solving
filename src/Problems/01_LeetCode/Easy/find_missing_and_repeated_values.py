# https://leetcode.com/problems/find-missing-and-repeated-values/description/


from collections import defaultdict

"""
    Time Complexity:  O(n^2) + O(n^2)
    Time Complexity:  O(n^2)
"""
def findMissingAndRepeatedValues(grid: list[list[int]]) -> list[int]:
    # Get the size of the grid (assuming it's an n x n matrix)
    n = len(grid)
    # Dictionary to count occurrences of each number in the grid
    counter = defaultdict(int)

    # Count the occurrences of each number in the grid
    for i in range(n):
        for j in range(n):
            counter[grid[i][j]] += 1
    
    # Placeholder for the duplicate number (a) and the missing number (b)
    ans = [None, None]
    
    # Sum of unique numbers in the grid
    actual_sum = 0
    for k, v in counter.items():
        # Add the number to the sum
        actual_sum += k
        if v == 2:
            # - The number appearing twice (a) (duplicate)
            ans[0] = k
    
    # Compute the expected sum of numbers from 1 to n^2 (formula for sum of first m natural numbers)
    m = n * n
    expected_sum = m * (m + 1) // 2

    # Find the missing number (b) by subtracting the actual sum from the expected sum
    b = expected_sum - actual_sum
    ans[1] = b

    return ans


print(findMissingAndRepeatedValues([[1,3],[2,2]]))                # [2, 4]
print(findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))    # [9, 5]

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