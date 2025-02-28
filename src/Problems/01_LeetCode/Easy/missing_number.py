# https://leetcode.com/problems/missing-number/description/


"""
    Brute Force: Using Linear Search
        Time Complexity:  O(n^2)
        Space Complexity: O(1)
"""
def bruteForce(nums: list[int]) -> int:
    n = len(nums)
    # Check for the missing number in the range [0, n]
    for i in range(1, n+1):
        flag: bool = False
        for j in range(0, n):
            if i == nums[j]:
                flag = True
                break
        
        # Return the missing number when (`flag` = False)
        if not flag:
            return i
        
    # Default return (should never reach here) 
    return -1

"""
    Better: Using Set
        Time Complexity:  O(n) + O(n) => O(2n)
        Space Complexity: O(n)
"""
def better(nums: list[int]) -> int:
    # Convert to Set for O(1) search
    nums_set = set(nums)

    for i in range(len(nums) + 1):
        if i not in nums_set:
            return i
    
    return -1

"""
    Optimal: Sum Approach
        Time Complexity:  O(n)
        Space Complexity: O(1)
    ---------
    Steps:
      - Use formula `(n * (n + 1)) / 2` to calculate `expected sum` of 'n' natural numbers
      - Find `actual sum` of list's numbers
      - Find Difference between (`expected sum` - `actual sum`)
"""
def optiomal(nums: list[int]) -> int:
    # Get the length of the input list (contains numbers from 0 to n)
    n = len(nums)

    # Compute the expected sum of numbers from 0 to n
    # # Formula: Sum of first N natural numbers = (n * (n + 1)) // 2
    expected_sum = (n * (n + 1)) // 2

    # Compute the actual sum of the given list
    actual_sum = sum(nums)

    # The missing number is the difference between expected and actual sums
    return expected_sum - actual_sum

"""
    ** Better than SUM Approach **
    Why:
      - Lets assume (n = 10**5)
      - Then, Sum = (10**5 + 10**5 + 1) / 2
      - This results in a very large number (~5 * 10**9)), 
        which can lead to integer overflow in some languages like C++ and Java.

    Optimal: Using XOR (⊕ or ^)
        Time Complexity:  O(n)
        Space Complexity: O(1)
    
    Steps:
      - [3, 0, 1]
      - XOR 1: 0 ^ 1 ^ 2 ^ 3
      - XOR 2: 0 ^ 1 ^ 3
      
      Answer:
        = (1 ^ 1) ^ 2 ^ (3 ^ 3)
        = 0 ^ 2 ^ 0
        = 2 
"""
def optiomal_2(nums: list[int]) -> int:
    # Get the length of the input list
    n: int = len(nums)

    # Initialize XOR variables
    XOR_1 = 0

    # Compute XOR of all indices (0 to n-1) and array elements
    for i in range(0, n):
        XOR_1 ^= (i + 1)    # XOR all numbers from 1 to n (expected full range)
        XOR_1 ^= nums[i]    # XOR all elements in the given list
    
    # Return the missing number
    # Since `XOR_1` now holds the missing number (due to cancellation of duplicates)
    return XOR_1

# Main Function
def missingNumber(nums: list[int]) -> int:

    print("Brute Force: (Linear)", bruteForce(nums))
    print("Better: (Set)",better(nums))
    print("Optimal: (Sum)", optiomal(nums))
    print("Optimal: (XOR)", optiomal_2(nums))
    

missingNumber([3, 0, 1])
print()
missingNumber([0, 2, 1])
print()
missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])



"""
    -----------
    Example 1:

        Input: nums = [3,0,1]
        Output: 2
        Explanation:
            n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
            2 is the missing number in the range since it does not appear in nums.
    -----------    
    Example 2:
        Input: nums = [0,1]    
        Output: 2
        Explanation:
            n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
            2 is the missing number in the range since it does not appear in nums.
    -----------    
    Example 3:
        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation:
            n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
            8 is the missing number in the range since it does not appear in nums.
    -----------
"""