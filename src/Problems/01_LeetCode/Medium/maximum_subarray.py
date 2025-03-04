# https://leetcode.com/problems/maximum-subarray/description/



"""
    Brute Force: Nested Loop
        Time Complexity:  O(n^2) => (Near n^2)
        Space Complexity: O(1)
"""
def brute_force(nums: list[int]) -> int:
    # Get the size of the array
    n = len(nums)

    # Initialize max_sum to the smallest possible integer value
    max_sum = float('-inf')
    for i in range(n):
        # Stores the sum of the current subarray
        curr_sum = 0

        # Iterate over all possible ending points of subarrays starting from `i`
        for j in range(i, n):
            # Add the current element to the subarray sum
            curr_sum += nums[j]
            # Update max_sum if we found a new maximum
            max_sum = max(curr_sum, max_sum)
    
    return max_sum


"""
    Optimal: Kadane's Algorithm
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int]) -> int:
    # Initialize the maximum sum with the smallest possible value
    max_sum = float('-inf')
    # Initialize current subarray sum to 0
    curr_sum = 0
    
    # Iterate through the array
    for num in nums:
        # Add the current element to the running sum
        curr_sum += num

        # Update max_sum if the current sum is greater than the previously recorded max_sum
        if curr_sum > max_sum:
            max_sum = max(curr_sum, max_sum)
        
        # If the running sum becomes negative, reset it (negative sums don't contribute to max sum)
        if (curr_sum < 0):
            curr_sum = 0
    
    return max_sum


# Print sub-array
def optimal_with_print_subarray(nums: list[int]) -> int:
    # Initialize the maximum sum with the smallest possible value
    max_sum = float('-inf')
    # Initialize current subarray sum to 0
    curr_sum = 0
    
    start, ans_start, ans_end = 0, -1, -1
    # Iterate through the array
    for i, num in enumerate(nums):
        # Wehenever `current sum = 0` that is starting point of sub-array
        if (curr_sum == 0):
            start = i

        # Add the current element to the running sum
        curr_sum += num
        
        # Update max_sum if the current sum is greater than the previously recorded max_sum
        if curr_sum > max_sum:
            max_sum = max(curr_sum, max_sum)
            ans_start, ans_end = start, i
        
        # If the running sum becomes negative, reset it (negative sums don't contribute to max sum)
        if (curr_sum < 0):
            curr_sum = 0
        
    # Print sub-array
    print(nums[ans_start : ans_end + 1])
    print()

# Main Function
def maxSubArray(nums: list[int]) -> int:
    # print(brute_force(nums))
    
    print(optimal(nums))
    optimal_with_print_subarray(nums)


maxSubArray([1])                        # 2
maxSubArray([-1])                       # -1
maxSubArray([5,4,-1,7,8])               # 23
maxSubArray([-2,1,-3,4,-1,2,1,-5,4])    # 6


"""
    ----------
    Example 1:
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: The subarray [4,-1,2,1] has the largest sum 6.
    ----------
    Example 2:    
        Input: nums = [1]
        Output: 1
        Explanation: The subarray [1] has the largest sum 1.
    ----------
    Example 3:    
        Input: nums = [5,4,-1,7,8]
        Output: 23
        Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
    
"""