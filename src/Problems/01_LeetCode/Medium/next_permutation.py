# https://leetcode.com/problems/next-permutation/description/


"""
    Time Complexity:  O(n) + O(n) + O(n) => O(3n)
    Spcae Complexity: O(1) -> (Modifies the list in place without extra storage)
"""
def nextPermutation(nums: list[int]) -> None:
    # Get the length of the array
    n = len(nums)

    # Find the breakpoint (first decreasing element from the right)
    breakpoint_idx = -1
    # Traverse from the second last element to the first
    for i in range(n - 2, -1, -1):
        # Find the first decreasing element
        if nums[i] < nums[i + 1]:
            breakpoint_idx = i
            break    # Found the breakpoint, exit loop

    # If no breakpoint is found, the array is sorted in descending order
    # Return the sorted array (smallest permutation)
    if breakpoint_idx == -1:
        nums.reverse()    # Reverse the entire list in place
        return nums
    

    # Find the smallest element greater than nums[breakpoint_idx] to swap
    swap_idx = -1
    for i in range(n - 1, breakpoint_idx, -1):
        if nums[i] > nums[breakpoint_idx]:
            swap_idx = i
            break
    # Swap the breakpoint element with the found element
    nums[breakpoint_idx], nums[swap_idx] = nums[swap_idx], nums[breakpoint_idx]

    # Reverse (sort) the part after the breakpoint index
    # Sorting to get the smallest next permutation
    # Since the suffix is always in descending order, reversing it would be optimal:
    # Reversing takes O(n), not O(n log n)
    nums[breakpoint_idx + 1:] = reversed(nums[breakpoint_idx + 1:])

    return nums


print(nextPermutation([1, 2, 3]))                # [1,3,2]
print(nextPermutation([1, 3, 2]))                # 
print(nextPermutation([3, 2, 1]))                # [1,2,3]
print(nextPermutation([1, 1, 5]))                # [1,5,1]
print(nextPermutation([2, 1, 5, 4, 3, 0, 0]))    #

"""
    Though Process:
    ---------------
    Example Input:
    [2, 1, 5, 4, 3, 0, 0]
    -----------------------
    Step-by-Step Breakdown:

    1. Find the Breakpoint
      - Identify the first decreasing element from the right
      - Here, nums[1] = 1 is the breakpoint because 1 < 5.
        [2, (1)] | [5, 4, 3, 0, 0]

    2. Find the Closest Greater Element
      - Find the smallest element larger than nums[1] = 1 on the right.
      - nums[4] = 3 is the closest greater element.
        [2, 1] | [5, 4, (3), 0, 0]

    3. Swap the Two Elements
        [2, 3] | [5, 4, 1, 0, 0]
          
    4. Sort the Elements After the Breakpoint
      - Sort the elements after index 1 (breakpoint index).
      - Final Output (Next Permutation):
        [2, 3, 0, 0, 1, 4, 5]

    [2,  3, 0, 0, 1, 4, 5] (Next Permutation)
"""

"""
    Next Permutation - > The next lexicographically greater arrangement of a set of elements
        [1, 2, 3]
      - [1, 3, 2] -> Greater than Previous one
      - [2, 1, 3] -> Greater than Previous one
      - [2, 3, 1] ...
      - [3, 1, 2] ...
      - [3, 2, 1] ...
"""

"""
    ----------
    ** Do not return anything, modify nums in-place instead. **
    ----------
    Example 1:
        Input: nums = [1,2,3]
        Output: [1,3,2]
    ----------
    Example 2:    
        Input: nums = [3,2,1]
        Output: [1,2,3]
    ----------
    Example 3:    
        Input: nums = [1,1,5]
        Output: [1,5,1]
    ----------
"""