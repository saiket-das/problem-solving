"""
    Contest Link: https://leetcode.com/contest/biweekly-contest-151/
"""

# https://leetcode.com/problems/transform-array-by-parity/

"""
    Time Complexity:  O(n log n) + O(n) => O(n log n)
    Space Complexity: O(n)
""" 
def transformArray(nums: list[int]) -> list[int]:
    # Replace `Odd` numbers with 1 and `Even` with 0
    new_arr = [num % 2 for num in nums]

    return sorted(new_arr)


print(transformArray([1, 2, 3, 4, 5, 6, 7]))