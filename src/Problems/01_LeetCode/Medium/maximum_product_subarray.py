# https://leetcode.com/problems/maximum-product-subarray/description/

from collections import defaultdict

"""
    Brute Force: Time Limit Exceeded
        Time Complexity:  O(n^2)
        Space Complexity: O(1)
"""
def brute_force(nums: list[int]) -> int:
    # Get the length of the list
    n = len(nums)

    # Initialize maximum product to negative infinity
    maximum = float('-inf')

    # Iterate through list
    for i in range(n):
        # Initialize product for the current subarray
        product = 1
        for j in range(i, n):
            # Multiply the current element to the product
            product *= nums[j]
            # Update the maximum product found so far
            maximum = max(maximum, product)
    
    return maximum


"""
    Optimal: 
        Time Complexity:  O(n) + O(n) => O(n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int]) -> int:
    # Get the length of the list
    n = len(nums)
    
    # Initialize variables to track the maximum product
    max_product = float('-inf')
    
    # `prefix` tracks the product of elements from the `left`
    # `suffix` tracks the product of elements from the `right`
    prefix, suffix = 1, 1

    # Iterate through the list
    for i in range(n):

        # Reset prefix product if it becomes zero
        if prefix == 0:
            prefix = 1
        
        # Reset suffix product if it becomes zero
        if suffix == 0:
            suffix = 1

        prefix *= nums[i]             # Update prefix product
        suffix *= nums[n - i - 1]     # Update suffix product

        # Update max_product with the highest value found so far
        max_product = max(max_product, prefix, suffix)
    

    return max_product

def maxProduct(nums: list[int]) -> int:
    # print(brute_force(nums))
    print(optimal(nums))


maxProduct([0,2])          # 2  -> [2]
maxProduct([1,2,3])        # 6  -> [1,2,3]
maxProduct([1,0,3])        # 3  -> [3]
maxProduct([3,-1,4])       # 4  -> [4]
maxProduct([-2,0,-1])      # 0  -> [0]
maxProduct([1,0,3,4])      # 12 -> [3,4]
maxProduct([2,3,-2,4])     # 6  -> [2,3]
maxProduct([1] * 10000)    # 1