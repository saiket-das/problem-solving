# https://leetcode.com/problems/contains-duplicate/description/


"""
    :type nums: List[int]
    :rtype: bool
"""

# Time Complexity: O(N)
def containsDuplicate(nums):
    # Initialize a frequency dictionary with sets to keep track of number frequencies
    freq_dict = {}

    for num in nums:    # TC: O(N)
        # If Num is already in Dict then return False
        # (Need to check .get(num) == num) because the number could be 0, 
        # # which would be considered False in a boolean context. 
        # # This ensures that 0 is handled correctly, as it can be a valid value in the dictionary.
        if (freq_dict.get(num) == num):    # TC: O(1)
            return True
        # If Num not in Dict then add that Num to DIct
        else:
            freq_dict[num] = num    # TC: O(1)
    
    for x in freq_dict:
        print(x)
    return False

print(containsDuplicate([0,4,5,0,3,6]))



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
