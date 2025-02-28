# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/


"""
    Time Complexity:  O(n)
    Space Complexity: O(1) 
"""
def check(nums: list[int]) -> bool:
    # Length of List
    n = len(nums)
    # Count how many times order breaks
    rotation_count = 0

    for i in range(n):
        # Circular indexing to wrap around at the end
        next_idx = (i + 1) % n
        
        # Check if the next element is smaller than the current element
        if (nums[next_idx] < nums[i]):
            rotation_count += 1
            # If more than one break in order, it's neither sorted nor a valid rotation
            if (rotation_count > 1):
                return False
            
    # Valid rotated sorted or already sorted list
    return True

print(check([6,10,6]))
# print(check([1, 2, 2, 3]))


"""
    Approach
      - Initialize List length and Count = 0
      - Iterate though array
      - Check current and next value 
          - if (nums[i+1 % n] < num[i]) => count ++  ( why i+1 % n, if `i` = 4 then next index `i+1 = 5 % 5 => 0`)
              - if (count > 1) return False

    Example 1:
        [3, 4, 5, 1, 2]
          - 4 ≮ 3 ✅ => count = 0
          - 5 ≮ 4 ✅ => count = 0
          - 1 < 5 ❌ => count = 1
          - 3 ≮ 3 ✅ => count = 1
          - 5 ≮ 4 ✅ => count = 1 
        return True
    
    Example 1:
        [2, 1, 3, 4]
          - 1 < 2 ❌ => count = 1
          - 3 ≮ 1 ✅ => count = 1
          - 4 ≮ 3 ✅ => count = 1
          - 2 < 4 ❌ => count = 2 ->  count > 1: return False
"""

"""
    ----------
    Example 1:
        Input: nums = [3,4,5,1,2]
        Output: true
        Explanation: [1,2,3,4,5] is the original sorted array.
        You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].
    ----------
    Example 2:
        Input: nums = [2,1,3,4]
        Output: false
        Explanation: There is no sorted array once rotated that can make nums.
    ----------
    Example 3:
        Input: nums = [1,2,3]
        Output: true
        Explanation: [1,2,3] is the original sorted array.
        You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
"""