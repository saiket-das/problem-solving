# https://leetcode.com/problems/single-number/description/

from collections import defaultdict

"""
    Brute Force: Using Hashmap or Dict
        Time Complexity:  O(n) => Two passes: One for counting, One for checking
        Sapce Complexity: O(n/2 + 1) => O(n) -> Extra space for the hashmap
"""
def brute_force(nums: list[int]) -> int:
    # Dictionary to store frequency of each number
    hashmap = defaultdict(int)

    # Count occurrences of each number  
    for num in nums:
        hashmap[num] += 1
    
    # Find the element that appears only once  
    for key, value in hashmap.items():
        if (value == 1):
            # Return the first unique element found
            return key


"""
    Optimal: Using XOR
        Time Complexity:  O(n) => Single pass through the array  
        Sapce Complexity: O(1) => No extra space used 
    
    Concepts
      - The XOR of two same numbers is 0 (e.g., `a ⊕ a = 0`).
      - When we XOR all elements, duplicate numbers cancel out, leaving only the unique one.
"""    
def optimal(nums: list[int]) -> int:
    # Initialize XOR variable
    XOR: int = 0

    # Compute XOR for all elements  
    for num in nums:
        # Cancel out duplicates, leaving only the unique number
        XOR ^= num
    
    # Return the unique number
    return XOR

def singleNumber(nums: list[int]) -> int:
    # print(brute_force(nums))
    print(optimal(nums))
    

singleNumber([2, 2, 3])
singleNumber([4, 1, 2, 1, 2])
singleNumber([1])
"""
    ----------
    Example 1:
        Input: nums = [2,2,1]
        Output: 1
    ----------   
    Example 2:    
        Input: nums = [4,1,2,1,2]
        Output: 4
    ---------- 
    Example 3:    
        Input: nums = [1]
        Output: 1
    ----------
"""