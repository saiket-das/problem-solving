# https://leetcode.com/problems/contains-duplicate/description/


"""
    :type nums: List[int]
    :rtype: bool
"""

"""
    Time Complexity:  O(N)
    Space Complexity: O(N)
"""
def containsDuplicate(nums: list[int]) -> bool:
    # Initialize an empty set to track seen numbers
    num_set = set()

    # Iterate through each number in the input list
    for num in nums:
        # Check if the current number is already in the set
        if (num in num_set):
            # If duplicate found, return True
            return True
        else:
            # If not a duplicate, add the number to the set
            num_set.add(num)
        
    # If no duplicates are found, return False
    return False

print(containsDuplicate([1,2,3,1]))



"""
    Example 1:
        Input: nums = [1,2,3,1]
        Output: true
        Explanation: The element 1 occurs at the indices 0 and 3.
    -------------
    Example 2:
        Input: nums = [1,2,3,4]
        Output: false
        Explanation:
        All elements are distinct.
    -------------
    Example 3:
        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true
"""
