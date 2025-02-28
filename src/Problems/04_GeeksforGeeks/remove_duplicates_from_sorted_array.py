# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from sortedcontainers import SortedSet 


"""
    Approach 1:
        Time Complexity:  O(n log n) + O(n)
        Space Complexity: O(n)
    
    Approach 2:
        Time Complexity:  O(n)
        Space Complexity: O(1)   
"""
def removeDuplicates(nums: list[int]) -> int:
    # Approach 1 - Brute force (Using Sorted Set)
    """
    # Create a sorted set to remove duplicates and maintain order
    nums_set = SortedSet(nums)    # TC: O(n log n) and SC: O(n)

    # Copy unique sorted elements back to `nums`
    i: int = 0
    for num in nums_set:    # TC: O(n)
        nums[i] = num
        i += 1

    # Return the number of unique elements
    return len(nums_set)
    """

    # Approach 2 - Optimal (Two Pointer)
    """
        -1, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4
        L   H

    """
    # `low` tracks the last unique element's position
    # `high` is used to iterate through the list
    low, high = 0, 1

    # `i` keeps track of the position for inserting unique elements
    i: int = 1

    # Traverse the list from the second element
    while (high < len(nums)):
        # Found a new unique element
        if (nums[low] != nums[high]):
            # Update `low` to point to this new unique element
            low = high
            # Place the unique element in its correct position
            nums[i] = nums[low]
            # Move to the next index for the next unique element
            i += 1
        
        # Always move `high` forward to check the next element
        high += 1
    
    # The new length of the array with unique elements
    return i


print(removeDuplicates([-1,0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([-1,0,0,0,0,3,3]))
print(removeDuplicates([1,1,2]))


"""
    ----------
    Example 1:
        Input: nums = [1,1,2]
        Output: 2, nums = [1,2,_]
        Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
                     It does not matter what you leave beyond the returned k (hence they are underscores).
    ----------
    Example 2:
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
                     It does not matter what you leave beyond the returned k (hence they are underscores).
    ----------
"""