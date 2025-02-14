

"""
    :type nums: List[int]
    :rtype: int
"""

def subarraySum( nums):
    total_sum = nums[0]
    n = len(nums)

    return total_sum

print(subarraySum([2, 3, 4, 5]))
# [2, 3, 1] -> 11
# [3, 1, 1, 2] -> 13

"""
   list[0] + list[1]
   list[1] + list[2]
   list[1] + list[2] + list[3]
   []
"""

"""
    Example 1 ([2, 3, 1] -> 11)
        1) Sum = 2
        2) 2 + 3 = 5, Sum = (2 + 5) = 7
        3) 3 + 1 = 4, Sum = (7 + 4) = 11
    -------------------
    Example 2 ([3, 1, 1, 2] -> 13)
        1) Sum = 3
        2) 3 + 1 = 4, Sum = (3 + 4) = 7
        3) 1 + 1 = 2, Sum = (7 + 2) = 9
        3) 1 + 2 = 3, Sum = (7 + 2) = 11
"""