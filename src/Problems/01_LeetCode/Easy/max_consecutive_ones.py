# https://leetcode.com/problems/max-consecutive-ones/description/


"""
    Time Complexity:  O(n)
    Space Complexity: O(1)
"""
def findMaxConsecutiveOnes(nums: list[int]) -> int:
    # Initialize variables
    # `count` tracks consecutive 1s, `maximum` stores the longest streak
    count, maximum = 0, 0

    # Iterate through the list  
    for num in nums:
        if num == 0:
            # Reset `count` when encountering 0
            count = 0
        else:
            # Increase `count` for consecutive 1s
            count += 1
        
        # Update the maximum streak found so far 
        maximum = max(count, maximum)
    
    # Return the longest sequence of consecutive 1s  
    return maximum


print(findMaxConsecutiveOnes([1,1,1,1,0,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))
"""
    ----------
    Example 1:
        Input: nums = [1,1,0,1,1,1]
        Output: 3
        Explanation: The first two digits or the last three digits are consecutive 1s. 
                     The maximum number of consecutive 1s is 3.
    ----------
    Example 2:
        Input: nums = [1,0,1,1,0,1]
        Output: 2
    ----------
"""