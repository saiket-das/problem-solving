# https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809
# /1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k


"""
    Brute Force: Using Nested Loop
        Time Complexity:  O(n^2) => Near N^2
        Sapce Complexity: O(1)   => No extra space used 
    
    Steps:
      - Find all Sub Arrays
      - Count their current_sum
      - If (current_sum == target), comapre length with previous longest length
    
    arr[] = [10, 5, 2, 7, 1, -10], k = 15
      - [10, 5, 2, 7, 1, -10]
      - [10], [10, 5], [10, 5, 2], ....
      - [5], [5, 2, [5, 2, 7], ....
""" 
def brute_force(arr, target): 
    n = len(arr)

    max_length = 0
    # Iterate through each starting index
    for i in range(n):
        current_sum = 0

        # Expand subarray from the starting index
        for j in range(i, n):
            current_sum += arr[j]

            # Check if the current subarray sum matches the target
            if (current_sum == target):
                max_length = max(max_length, j - i + 1)

    return max_length      
                

"""
    Better: Using HashMap
        Time Complexity:  O(n) => (But can degrade to O(n²) in case of extreme hash collisions, but rare)
        Sapce Complexity: O(n)
""" 
def better(arr, k):
    # Stores the first occurrence of each prefix sum
    prefix_sum_map: dict = {}
    max_length, current_sum = 0, 0

    for i in range(len(arr)):
        # Update the cumulative sum
        current_sum += arr[i]

        # If the entire subarray from 0 to index sums to target, update max_length
        if current_sum == k:
            max_length = max(max_length, i + 1)
        
        # Check if removing a prefix sum results in the target sum
        rem = current_sum - k
        if rem in prefix_sum_map:
            length = i - prefix_sum_map[rem]
            max_length = max(max_length, length)
        
        # Store the first occurrence of the current prefix sum
        if current_sum not in prefix_sum_map:
            prefix_sum_map[current_sum] = i
    
    return max_length


"""
    Optimal: Two Pointer (Sliding Window) -> (Optimal solution for only Positive and Zero elements)
        Time Complexity:  O(n) + O(n) => O(n) -> Single pass through the array  
        Sapce Complexity: O(1) -> → No extra space used 
"""
def optimal(arr, k): 
    n = len(arr)
    
    left, right = 0, 0
    max_length = 0
    # Initialize sum with the first element if array is not empty
    current_sum = arr[0] if arr else 0  

    while right < n:
        # Shrink window from the left if the sum exceeds the target
        while left <= right and current_sum > k:
            current_sum -= arr[left]
            left += 1
        
        # Update maximum length if the current window matches the target sum
        if (current_sum == k):
            max_length = max(max_length, right - left + 1)
        
        # Expand window from the right
        right += 1
        if right < n:
            current_sum += arr[right]
        
        
    return max_length

# Main Function
def longestSubarray(arr, k): 
    # print(brute_force(arr, k))
    # print(better(arr, k))

    # Optimal solution for only Positive and Zero elements
    print(optimal(arr, k))

longestSubarray([10, 5, 2, 7, 1, -10], 15)
longestSubarray([-5, 8, -14, 2, 4, 12], -5)
longestSubarray([10, -10, 20, 30], 5)
longestSubarray([10, -10, 10, -10, 10, 10, -10, -10, 20, -10, -10, 30], 0)
longestSubarray([2, 0, 0, 3], 3)
longestSubarray([1, 2, 3, 1, 1, 1, 1], 3)

"""
    ----------
    Example 1:
        Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
        Output: 6
        Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. 
                     The length of the longest subarray with a sum of 15 is 6.
    ----------   
    Example 2:
        Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
        Output: 5
        Explanation: Only subarray with sum = -5 is [-5, 8, -14, 2, 4] of length 5.
    ----------
    Example 3:
        Input: arr[] = [10, -10, 20, 30], k = 5
        Output: 0
        Explanation: No subarray with sum = 5 is present in arr[].
    ----------
"""