# https://www.interviewbit.com/problems/subarray-with-given-xor/


"""
    Brute Force: Nested Loop
        Time Complexity:  O(n * n)
        Space Complexity: O(1)
"""
from collections import defaultdict


def brute_force(arr, target):
    # Get the length of the array
    n = len(arr)

    # Variable to store the count of subarrays where the XOR equals the target value
    count = 0

    # Iterate through each element as the starting point of the subarray
    for i in range(n):
        # If a single element matches the target XOR, count it
        if arr[i] == target:
            count += 1

        # Initialize a variable to store the cumulative XOR from index i to j
        k = arr[i]

        # Expand the subarray and compute XOR for all possible subarrays starting at i
        for j in range(i + 1, n):
            # Compute the XOR of the subarray arr[i...j]
            k = k ^ arr[j]

            # If the computed XOR matches the target, increment the count
            if k == target:
                count += 1

    # Return the total count of subarrays with the required XOR value            
    return count


"""
    Optimal: Nested Loop
        Time Complexity:  O(n)
        Space Complexity: O(n)
    
    Formula
        x ^ k = prefix_xor
        x = prefix_xor ^ k
"""
def optimal(nums, target):
    # Variable to store the count of subarrays where the XOR equals the target value
    subarray_count = 0

    # Stores frequency of prefix XOR values
    prefix_xor_freq = defaultdict(int)
    # Current prefix XOR
    prefix_xor = 0
    # Initialize with XOR 0 appearing once
    prefix_xor_freq[prefix_xor] += 1

    # Iterate through the array
    for num in nums:   
        # Update prefix XOR     
        prefix_xor ^= num 

        # Check if there's a prefix XOR that satisfies prefix_xor ^ required_xor = target
        required_xor = prefix_xor ^ target
        if required_xor in prefix_xor_freq:
            subarray_count += prefix_xor_freq[required_xor]

        # Store the frequency of the current prefix XOR 
        prefix_xor_freq[prefix_xor] += 1
    
    return subarray_count



# Main Function
def solve(nums, target):
    # print(brute_force(arr, xor))
    print(optimal(nums, target))


solve([4, 2, 2, 6, 4], 6)    # 4
solve([5, 6, 7, 8, 9], 5)    # 2
solve([1, 2, 3, 4, 5], 7)    # 1