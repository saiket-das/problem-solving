# https://leetcode.com/problems/3sum/description/



   
"""
    Approach 1: Brute Force
        Time Complexity:  O(n^3)
        Space Complexity: O(1)
"""
    # result = [list]
    # n = len(nums)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         for k in range(j+i, n):
    #             three_sum = nums[i] + nums[j] + nums[k]
    #             if (three_sum == 0 and i != j and i!=k  and j != k):
    #                 result.append([nums[i], nums[j], nums[k]]) 
    
"""
    Time Complexity:  O(n^2)
    Space Complexity: O(1) 
    
    Approach
        1. **Sorting the array**  
           - Sorting helps in avoiding duplicate triplets efficiently.
           - It also allows using the **Two-Pointer Technique**.
    
        2. **Iterating through the array**  
           - If `nums[i] > 0`, break the loop (as positive numbers can't sum to zero).
           - If `nums[i]` is a duplicate (`nums[i] == nums[i-1]`), **skip** to avoid duplicate triplets.
    
        3. **Two-Pointer Technique**  
           - Use `l` (left pointer) and `r` (right pointer) to find a triplet.
           - Compute `three_sum = nums[i] + nums[l] + nums[r]`:
              - If `three_sum < 0`, **increase left** (`l += 1`).
              - If `three_sum > 0`, **decrease right** (`r -= 1`).
              - If `three_sum == 0`, **store triplet and update pointers**.
              - Skip duplicates to avoid redundant triplets.
"""

def threeSum(nums: list[int]) -> list[list[int]]:
    # Sort the array
    nums.sort()
    n = len(nums)
    result = []
    # Iterate though the array
    for i in range(n):
        # If current number is greater than 0, break (no way to sum to zero)
        if (nums[i] > 0):
            break
        
        # Skip duplicate elements to avoid duplicate triplets
        if (i > 0 and nums[i] == nums[i - 1]):
            continue
        
        # Two-pointer approach
        l, r = i + 1, n - 1
        while (l < r):
            three_sum: int = nums[i] + nums[l] + nums[r]
            # Increase left pointer to get a larger sum
            if (three_sum < 0):
                l += 1
            # Decrease right pointer to get a smaller sum
            elif (three_sum > 0):
                r -= 1
            else:
                # Found a valid triplet (append to `result`)
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # Skip duplicate values for `l` (if current and next `l` element are same) 
                while (nums[l] == nums[l - 1] and l < r):
                    l += 1

    
    return result
    

print(threeSum([-1, 0, 1, 2, -1, -4]))



"""
    ** Notice that the solution set must not contain duplicate triplets. ❌ ** 
    -----------
    Example 1:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Explanation: 
          - nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
          - nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
          - nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.
    -----------
    Example 2:
        Input: nums = [0,1,1]
        Output: []
        Explanation: The only possible triplet does not sum up to 0.
    -----------
    Example 3:
        Input: nums = [0,0,0]
        Output: [[0,0,0]]
        Explanation: The only possible triplet sums up to 0.
    -----------
"""