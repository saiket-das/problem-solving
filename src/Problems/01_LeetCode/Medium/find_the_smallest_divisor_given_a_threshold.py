# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/


"""
"""
import math


"""
    Brute Force: 
        Time Complexity:  O(n) + O(max(nums) * n)
        Space Complexity: O(1)
"""
def brute_force(nums: list[int], threshold: int) -> int:
    # Find the largest possible divisors from the list
    max_divisor = max(nums)


    # Iterate over all possible divisors in the range [min_divisor, max_divisor]
    for divisor in range(1, max_divisor + 1):
        # Stores the sum of divisions for the current divisor
        divisor_sum = 0

        # Compute the sum of ceiling division results for all numbers
        for num in nums:
            divisor_sum += math.ceil(num / divisor)
        
        # If the sum does not exceed the threshold, return the smallest valid divisor
        if divisor_sum <= threshold:
            return divisor

    # This line will never execute because test cases guarantee a valid answer
    return 0 




"""
    Optimal: 
        Time Complexity:  O(n) + O(log max(nums) * n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int], threshold: int) -> int:
    # Find the largest possible divisors from the list
    max_divisor = max(nums)

    # Initialize binary search boundaries
    low, high = 1, max_divisor

    # Perform binary search
    while low <= high:
        # `mid` as the current divisor candidate
        mid = (low + high) // 2

        # Stores the sum of ceiling division results for all numbers
        divisor_sum = 0

        # Compute the total sum of divisions
        for num in nums:
            divisor_sum += math.ceil(num / mid)
        
        # If the divisor sum is within the threshold, search for a smaller divisor
        if divisor_sum <= threshold:
            high = mid - 1    # Try a smaller divisor
        else:
            low =  mid + 1    # Increase the divisor to reduce the sum

    # The smallest divisor that satisfies the condition is stored in `low`
    return low




# Main Function
def smallestDivisor(nums: list[int], threshold: int) -> int:
    print(brute_force(nums, threshold))
    print(optimal(nums, threshold))


smallestDivisor([1,2,5,9], 6)          # 5
smallestDivisor([44,22,33,11,1], 5)    # 44
smallestDivisor([21212,10101,12121], 3)