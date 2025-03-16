# https://leetcode.com/problems/running-sum-of-1d-array/description/


"""
    Brute Force: Nested Loop
        Time Complexity:  O(n * n)
        Space Complexity: O(n)
"""
def brute_force(nums: list[int]) -> list[int]:
    # Get the length of the input list
    n = len(nums)

    # Initialize the result list with the first element of nums
    result = []
    
    # Iterate through each index `i` in the list
    for i in range(n):
        # Initialize the current sum with the value at index `i`
        curr_sum = nums[i]
        # Add all previous elements from index `0` to `i-1`
        for j in range(0, i):
            curr_sum += nums[j]
        
        # Store the computed prefix sum in the result list
        result.append(curr_sum)
    
    # Return the list containing prefix sums
    return result


"""
    Better:
        Time Complexity:  O(n)
        Space Complexity: O(n)
"""
def better(nums: list[int]) -> list[int]:
    # Get the length of the input list
    n = len(nums)

    # Initialize the result list with the first element of nums
    result = [nums[0]]
    # Initialize prefix_sum with the first element
    prefix_sum = nums[0]

    # Iterate through the list starting from the second element
    for i in range(1, n):
        # Add the current element to the running sum
        prefix_sum += nums[i]
        # Append the updated prefix sum to the result list
        result.append(prefix_sum)
    
    # Return the list containing prefix sums
    return result


"""
    Optimal:
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int]) -> list[int]:
    # Get the length of the input list
    n = len(nums)

    # If the list is empty, return an empty list
    if n == 0:
        return []
    
    # Iterate through the list starting from the second element
    for i in range(1, n):
        # Compute the prefix sum by adding the previous sum to the current element
        nums[i] = nums[i - 1] + nums[i]
    
    # Return the modified list containing prefix sums
    return nums


# Main Function
def runningSum(nums: list[int]) -> list[int]:
    print(brute_force(nums))
    # print(better(nums))
    # print(optimal(nums))


runningSum([1,2,3,4])       # [1,3,6,10]
runningSum([1,1,1,1,1])     # [1,2,3,4,5]
runningSum([3,1,2,10,1])    # [3,4,6,16,17]