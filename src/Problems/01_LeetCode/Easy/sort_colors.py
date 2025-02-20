# https://leetcode.com/problems/sort-colors/description/

"""
    Time Complexity:  O(NlogN)
    Space Complexity: O(n)
"""

# ---- Divide ----
def divide(nums: list[int], low: int, high: int):
    if (low >= high):
        return
    mid = (low + high) // 2
    divide(nums, low, mid)
    divide(nums, mid + 1, high)
    
    merge(nums, low, mid, high)

# ---- Merge ----
def merge(nums: list[int], low: int, mid: int, high: int):
    temp: list[int] = []

    left: int = low
    right: int = mid + 1

    while ((left <= mid) and (right <= high)):
        if (nums[left] <= nums[right]):
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
    
    while (left <= mid):
        temp.append(nums[left])
        left += 1
    while (right <= high):
        temp.append(nums[right])
        right += 1
    
    for i in range(low, high + 1):
        nums[i] = temp[i - low]



def twoPointer(nums: list[int]):
    """
        Rules:
        1. If nums[i] == 0 → Swap with nums[l] and move both `l` and `i` forward.
        2. If nums[i] == 2 → Swap with nums[r`], move `r` backward (but don't move `i` to recheck swapped value).
        - If nums[i] == 1 → Just move `i` forward.
    """
    l: int = 0                # Left pointer
    r: int = len(nums) - 1    # Right pointer
    i: int = 0                # Iterator pointer

    # Continue until the iterator (i) crosses the right pointer (r)
    while (i <= r):
        # Rule 1
        if (nums[i] == 0):
            # Swap current element with left pointer and move both forward
            nums[l], nums[i] = nums[i], nums[l]
            l += 1    # Move to the next element
        # Rule 2
        if (nums[i] == 2):
            # Swap current element with right pointer and move right backward
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1    # Reduce right pointer
        i += 1
    
"""
    Approach 1: Sorting Algorithms
        Time Complexity:  O(NlogN)
        Space Complexity: O(N) ❌
    Approach 2: Two Pointer
        Time Complexity:  O(N)
        Space Complexity: O(1) ✅ -> (Sorting is done in-place)
"""

def sortColors(nums: list[int]) -> None:
    # Approach 1:
    # low, high = 0, len(nums) - 1
    # divide(nums, low, high)

    # Approach 2:
    twoPointer(nums)
    print(nums)

sortColors([1,0,2])

"""
    [2,0,2,1,1,0]
    [2,0,1]
    [1,0,2]
"""

""" 
    ** Follow up: Could you come up with a one-pass algorithm using only constant extra space? **
        Space Complexity: O(1)

    - Do not return anything, modify nums in-place instead.

    - Constraints:
        n == nums.length
        1 <= n <= 300
        nums[i] is either 0, 1, or 2
"""

""" 
    ----------
    Example 1:
        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
    ----------
    Example 2:    
        Input: nums = [2,0,1]
        Output: [0,1,2]
    ----------
"""
    