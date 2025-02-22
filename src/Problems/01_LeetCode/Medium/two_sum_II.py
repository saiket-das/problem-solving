# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


"""
    Time Complexity:  O(n)
    Space Complexity: O(1)
"""

# Using Two Pointer
def twoSum( numbers: list[int], target: int) -> list[int]:
    # Initialize two pointers (Left and Right)
    l, r = 0, len(numbers)-1

    # Iterate until pointers meet
    while (l <= r):
        # Compute sum of two numbers
        sum = numbers[l] + numbers[r]
        # If Target found, Convert to 1-based index and return
        if (sum == target):
            return [l+1, r+1]
        
        # Adjust pointers based on sum comparison
        if (sum < target):
            l += 1    # Move left pointer forward to increase sum
        else:
            r -= 1    # Move right pointer backward to decrease sum
    
    # In case no valid pair is found 
    return []


print(twoSum([-1,0], -1))


"""
   ** `numbers` array is already sorted in non-decreasing order **
   ** Your solution must use only constant extra space. -> O(1) **
    ----------
    Example 1:
        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
    ----------    
    Example 2:
        Input: numbers = [2,3,4], target = 6
        Output: [1,3]
        Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
    ----------
    Example 3:
        Input: numbers = [-1,0], target = -1
        Output: [1,2]
        Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
    ----------
"""