# https://leetcode.com/problems/rotate-array/description/


"""
    Time Complexity:  O(n) + O(k) + (n - k) -> O(2n)
    Space Complexity: O(1)
"""

# Right Rotate
def rotate( nums: list[int], k: int) -> None:
    # Get the length of the list
    n = len(nums)
    k %= n  # Reduce unnecessary full rotations
    
    # Reverse the entire list -> TC: O(N)
    nums.reverse()
    # Reverse the elements before `k` index -> O(k)
    nums[:k] = reversed(nums[:k])
    # Reverse the elements from `k` index to `n - 1` -> TC: O(n - k)
    nums[k:] = reversed(nums[k:])


    # Rotate Left
    # nums[:k+1] = reversed(nums[:k+1])
    # nums[k+1:] = reversed(nums[k+1:])


rotate([1,2,3,4,5,6,7], 3)

"""
    - Original list
        [1, 2, 3, 4, 5, 6, 7]
    - Reverse the entire list
        [7, 6, 5, 4, 3, 2, 1]
    - Reverse the elements before `k` index
        [5, 6, 7, 4, 3, 2, 1]
    - Reverse the elements from `k` index to `n - 1`
        [5, 6, 7, 1, 2, 3, 4]
"""
    
"""
    [1, 2, 3, 4, 5, 6, 7], k = 3
    [4, 5, 6, 7, 1, 2, 3]
    
"""

"""
    ----------
    Example 1:
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        Explanation: rotate 1 steps to the right: [7,1,2,3,4,5,6]
                     rotate 2 steps to the right: [6,7,1,2,3,4,5]
                     rotate 3 steps to the right: [5,6,7,1,2,3,4]
    ----------
    Example 2:
        Input: nums = [-1,-100,3,99], k = 2
        Output: [3,99,-1,-100]
        Explanation: rotate 1 steps to the right: [99,-1,-100,3]
                     rotate 2 steps to the right: [3,99,-1,-100]
    ----------
"""