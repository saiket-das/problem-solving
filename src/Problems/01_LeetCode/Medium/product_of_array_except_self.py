# https://leetcode.com/problems/product-of-array-except-self/

"""
    Approach 1:
        Time Complexity:  O(n^2)
        Space Complexity: O(n)
"""
def productExceptSelf(nums: list[int]) -> list[int]:
    N: int = len(nums)

    res = []
    for i in range(N):
        product: int = 1
        for j in range(N):
            if (i != j):
                product *= nums[j]
        res.append(product)

    return res

"""
    Approach 2:
        Time Complexity:  O(n) + O(n) = O(n)
        Space Complexity: O(n)
    
        Explanation:
            [1, 2, 3, 4]
            ----------------------------------------------------
            Prefix  = [1, (1 * 2), (1 * 2 * 3), (1 * 2 * 3 * 4)]
                    = [1, 2, 6, 24] 
            ----------------------------------------------------
            Suffix  = [(1 * 2 * 3 * 4), (2 * 3 * 4), (3 * 4), 4]
                    = [24, 24, 12, 4]
            ----------------------------------------------------
            Product = Prefix[i-1] * Suffix[i+1]
                        [1, 2, 3, 4]         -> (Original Array)
                        (1) [1, 2, 6, 24]    -> (Assume, Prefix[-1] = 1)
                        (1) [24, 24, 12, 4]
                    ------------------------
                    i = -1   0   1   2   3   -> index (i)
                    ------------------------
                    (Prefix[i-1] * Suffix[i+1])  
                    - (1 * 24) = 24
                    - (1 * 12) = 12
                    - (2 * 4)  = 8
                    - (6 * 1)  = 6
        --------------------------------------------------------
"""
def productExceptSelf(nums: list[int]) -> list[int]:
    n: int = len(nums)

    result = [1] * n
    prefix_product = 1
    for i in range(n):
        result[i] = prefix_product
        prefix_product *= nums[i]
    
    
    suffix_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix_product
        suffix_product *= nums[i]

    return result


result = productExceptSelf([1, 2, 3, 4] )
print(result)


"""
    [1, 2, 3, 4] 
    [-1, 1, 0, -3, 3]
"""
"""
    -----------
    Example 1:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        Explanation:
          = [(2 * 3 * 4), (1 * 3 * 4), (1 * 2 * 4), (1 * 2 * 3)]
          = [24, 12, 8, 6]
    -----------
    Example 2:
        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]
    -----------
"""
