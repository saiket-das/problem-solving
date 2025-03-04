# https://leetcode.com/problems/two-sum/description/


"""
    Brute Force: Nested Loop
        Time Complexity:  O(n^2) 
        Space Complexity: O(1)   => No additional space used  
"""
def brute_force(nums: list[int], target: int):
    # Get the length of the input list
    n = len(nums)

    # Iterate over all possible pairs of elements
    for i in range(n):
        # Start from `i + 1` to avoid duplicate pairs
        for j in range(i + 1, n):
            # Check if the sum of the two elements equals the target
            if nums[i] + nums[j] == target:
                # Return the indices of the two elements
                return [i, j]
            


"""
    Optimal: HashMap
        Time Complexity:  O(n) => O(n log n) if Sorted hashmap
        Space Complexity: O(n)
"""
def optimal(nums: list[int], target: int):
    hashMap = {}  # <Element, Index of Element> -> {2: 0, 11: 1, 7: 2}
        
    for i in range(len(nums)):
        # Find the Complement element of Current element
        complement = target - nums[i]
        # If Complement Num is available in HASHMAP 
        # Then return the Index of Complement element and Current element's Index
        if (complement in hashMap):
            return [hashMap.get(complement), i]
        
        # If Complement element is not available in HashMap 
        # Then add Complement element into HashMap (<Element, Index of Element>)
        hashMap[nums[i]] = i



# Main Function
def twoSum(nums: list[int], target: int):
    print(brute_force(nums, target))
    print(optimal(nums, target))

twoSum([3,2,4], 6)

"""
    ** You may assume that each input would have exactly one solution, and you may not use the same element twice. *

    ----------
    Exmaple 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    ----------
    Exmaple 1:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
    ----------
    Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]
    ----------
"""

"""
    nums = [2,7,11,15], target = 9
      - hashMap = {}
      - Iterate through nums LIST or ARRAY
      - Find the COMPLEMENT number of current number
      - If COMPLEMENT Num is available in HASHMAP then return the INDEX of COMPLEMENT Num's and CURRENT Num's INDEX
      - If COMPLEMENT Num is not available in HASHMAP then add COMPLEMENT Num into HASHMAP like {NUM: INDEX of Num}
"""
        