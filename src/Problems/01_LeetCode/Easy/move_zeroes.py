# https://leetcode.com/problems/move-zeroes/description/


"""
    Approach 1: Brute Force
        Time Complexity:  O(n) + O(x) + O(n - x)
        Space Complexity: O(n) -> (Worst Case - All elements are non-zero) 
"""
def brute_force(nums: list[int]) -> None:
    temp = []
    # Save all non-zero number to `temp` list -> TC: O(n)
    for num in nums:
        if (num != 0):
            temp.append(num)
    
    # Replace `nums` list with `temp` list -> TC: O(x) (x = numbers of non-zero elements)
    for i, x in enumerate(temp):
        nums[i] = x
    
    # Replace remaining element with 0 -> TC: O(n - x)
    n = len(nums)
    temp_n = len(temp)
    for i in range(temp_n, n):
        nums[i] = 0


"""
    Approach 1: Two Pointer
        Time Complexity:  O(n) + O(n) => O(n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int]) -> None:
    # Length of the List
    n: int = len(nums)
    
    # Find the index of the first zero in the list
    # Time Complexity: O(n) (Worst case - If there is no zero, we traverse the entire list)
    j: int  = -1
    for i in range(n):
        if (nums[i] == 0):
            j = i
            break

    # If `j == -1`, it means there are no zeros in the list, so no need to process further
    if (j == -1):
        return
    
    # Move non-zero elements to the left while keeping the relative order of zeros (Using two-pointer approach)
    # Time Complexity: O(n) (Worst case - If the first element is zero, we swap for every non-zero element)
    for i in range(j + 1, n):
        if (nums[i] != 0):
            nums[i], nums[j] = nums[j], nums[i]
            j += 1    # Move the zero index forward


def moveZeroes(nums: list[int]) -> None:
    # brute_force(nums)
    optimal(nums)

    print(nums)


moveZeroes([2, 1, 2, 0, 3, 0, 12, 0])


"""
    Approach 1:
      - Save all non-zero number to `temp` list
      - Replace `nums` list with `temp` list
      - Replace remaining element with 0
"""

"""
    ----------
    Example 1:
        Input: nums = 
        Output: [1,3,12,0,0]
    ----------
    Example 2:
        Input: nums = [0]
        Output: [0]
    ----------
"""