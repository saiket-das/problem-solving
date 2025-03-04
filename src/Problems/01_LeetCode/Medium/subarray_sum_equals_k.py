# https://leetcode.com/problems/subarray-sum-equals-k/description/



"""
    Brute Force Approach: Using Nested Loop
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
from collections import defaultdict


def brute_force(arr, target): 
    n = len(arr)

    count = 0
    # Iterate through each starting index
    for i in range(n):
        current_sum = 0

        # Expand subarray from the starting index
        for j in range(i, n):
            current_sum += arr[j]

            # Check if the current subarray sum matches the target
            if (current_sum == target):
                count += 1

    return count      


"""
    Optimal Approach: Using HashMap + Prefix Sum
        Time Complexity:  O(n) => (But can degrade to O(n²) in case of extreme hash collisions, but rare)
        Sapce Complexity: O(n) => Stores prefix sums in a hashmap
"""
def optimal(nums: list[int], k: int) -> int:
    # Stores the first occurrence of each prefix sum
    prefix_sum_map = defaultdict(int)
    current_sum, count= 0, 0

    for i in range(len(nums)):
        # Update the cumulative sum
        current_sum += nums[i]

        # If the entire subarray from the start (index 0) to the current index sums to target
        if current_sum == k:
            count += 1
        
        # Check if removing a prefix sum results in the target sum, update `count``
        remaining_sum = current_sum - k
        if remaining_sum in prefix_sum_map:
            count +=  prefix_sum_map[remaining_sum]
        
        # Store the occurrence of the current prefix sum
        # This keeps track of how many times a certain prefix sum has been seen
        prefix_sum_map[current_sum] += 1
    
    return count


# Main Function
def subarraySum(nums: list[int], k: int) -> int:
    print(optimal(nums, k))

subarraySum([1, 1, 1], 2)
subarraySum([1, 2, 3], 3)
subarraySum([1, 2, 1, 2, 1], 3)
subarraySum([0,0,0,0,0,0,0,0,0,0], 0)