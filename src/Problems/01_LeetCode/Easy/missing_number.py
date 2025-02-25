# https://leetcode.com/problems/missing-number/description/



def missingNumber( nums: list[int]) -> int:
    """
        Approach 1:
            Time Complexity:  O(n)
            Space Complexity: O(n)

    # Convert the List into a Set for faster lookup
    nums_set = set(nums)

    # Check for the missing number in the range [0, n]
    for i in range(len(nums) + 1):
        if i not in nums_set:
            # Return the missing number when found
            return i
        
    # Default return (should never reach here) 
    return -1
    """

    """
        Approach 2:
            Time Complexity:  O(n)
            Space Complexity: O(n)
            ---------
            Steps:
              - Use formula (n(n + 1) / 2) to calculate `expected sum` of 'n' natural numbers
              - Find `actual sum` of list's numbers
              - Find Difference between (`expected sum` - `actual sum`)
    """
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum




print(missingNumber([9,6,4,2,3,5,7,0,1]))

"""
    
    -----------
    Example 1:

        Input: nums = [3,0,1]
        Output: 2
        Explanation:
            n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
            2 is the missing number in the range since it does not appear in nums.
    -----------    
    Example 2:
        Input: nums = [0,1]    
        Output: 2
        Explanation:
            n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
            2 is the missing number in the range since it does not appear in nums.
    -----------    
    Example 3:
        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation:
            n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
            8 is the missing number in the range since it does not appear in nums.
    -----------
"""