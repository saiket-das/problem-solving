# https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1?category%5B%5D=Hash&company%5B%5D=Amazon&page=1&query=category%5B%5DHashcompany%5B%5DAmazonpage1company%5B%5DAmazoncategory%5B%5DHash&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-subarray-with-0-sum



"""
    Brute Force: Nested Loop
        Time Complexity:  O(n^2)
        Space Complexity: O(1)
"""
def brute_force(nums: list) -> int:
    # Get the length of the list 
    n = len(nums)

    # Variable to store the length of the longest subarray with sum = 0
    largest = 0

    # Iterate through each element as the starting point of the subarray
    for i in range(n):
        # Initialize sum with the first element of the subarray
        summation = nums[i]

        # Expand the subarray by adding elements one by one
        for j in range(i + 1, n):
            # Add the current element to the sum
            summation += nums[j]

             # Check if the sum of the subarray [i...j] is zero
            if summation == 0:
                # Update largest length if the current subarray is longer
                largest = max(j - i + 1, largest)
    
    # Return the length of the longest subarray with sum = 0
    return largest



"""
    Optimal: HashMap
        Time Complexity:  O(n)
        Space Complexity: O(n)
"""
def optimal(nums: list) -> int:
    # Get the length of the list 
    n = len(nums)

    # Variable to store the length of the longest subarray with sum = 0
    largest = 0
 
    # Dictionary to store the first occurrence index of cumulative sums
    freq_dict = {}

    # Variable to keep track of the cumulative sum of elements
    curr_sum  = 0

    # Iterate through the list while maintaining the cumulative sum
    for i in range(n):
        # Update the cumulative sum
        curr_sum += nums[i] 

        # If the cumulative sum is 0, the entire subarray from index 0 to i has sum = 0
        if curr_sum == 0:
            # Update largest length
            largest = i + 1

        else:
            # If the same cumulative sum has been seen before, a zero-sum subarray exists
            if curr_sum in freq_dict:
                # Calculate the length of the subarray and update `largest` if it's longer
                largest = max(i - freq_dict[curr_sum], largest)
            else:
                # Store the first occurrence index of this cumulative sum
                freq_dict[curr_sum] = i
        
    
    # Return the length of the longest subarray with sum = 0
    return largest


# Main Function
def largestSubarrayWithZero(nums: list) -> int:
    # print(brute_force(nums))
    print(optimal(nums))


largestSubarrayWithZero([2, 10, 4])                       # 0
largestSubarrayWithZero([1, 0, -4, 3, 1, 0])              # 5
largestSubarrayWithZero([15, -2, 2, -8, 1, 7, 10, 23])    # 5
