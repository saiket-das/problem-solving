# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

"""
    Brute Force: Two-Pass or Bucket Sorting
        Time Complexity:  O(n) + O(n/2) => O(n)
        Space Complexity: O(n)
"""
def brute_force(nums: list[int]) -> list[int]:
    # Lists to separate positive and negative numbers
    pos_nums = []
    neg_nums = []

    # Categorize numbers into positive and negative lists
    for num in nums:
        if num < 0:
            neg_nums.append(num)
        else:
            pos_nums.append(num)
    
    # Since the input is assumed to have equal positive and negative numbers
    length = len(nums) // 2

    # Rearrange elements in the original list by placing positives and negatives alternately
    for i in range(length):
        nums[2 * i] = pos_nums[i]        # Add a positive number => (index: 0, 2, 4, .....)
        nums[2 * i + 1] = neg_nums[i]    # Add a negative number => (index: 1, 3, 5, .....)
        
    return nums


"""
    Optimal: Two Pointer
        Time Complexity:  O(n)
        Space Complexity: O(n)
"""
def optimal(nums: list[int]) -> list[int]:
    # Initialize indices for positive and negative numbers
    pos_idx, neg_idx = 0, 1

    # Create an empty list to store the rearranged numbers as same length as nums
    result = [0] * len(nums)

    # Iterate through the input list and place numbers at the correct positions
    for num in nums:
        if num < 0:
            # Place negative numbers at odd indices
            result[neg_idx] = num
            # Move to the next available odd index
            neg_idx += 2
        else:
            # Place positive numbers at even indices
            result[pos_idx] = num
            # Move to the next available even index
            pos_idx += 2
    
    return result
        



def rearrangeArray(nums: list[int]) -> list[int]:
    print(brute_force(nums))

rearrangeArray([3,1,-2,-5,2,-4])    # [3,-2,1,-5,2,-4]
rearrangeArray([-1,1])              # [1,-1]

"""
    ----------
    Example 1:
        Input: nums = [3,1,-2,-5,2,-4]
        Output: [3,-2,1,-5,2,-4]
        Explanation: The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
                     The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
                     Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect 
                     because they do not satisfy one or more conditions.  
    ----------
    Example 2:    
        Input: nums = [-1,1]
        Output: [1,-1]
        Explanation: 1 is the only positive integer and -1 the only negative integer in nums.
                     So nums is rearranged to [1,-1].
    ----------
"""