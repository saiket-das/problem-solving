# https://leetcode.com/problems/sort-colors/description/

"""
    Brute Force: Merge Sort (Divide and Conquer)
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



"""
    Better Approach: 
        Time Complexity:  O(n) + O(n) = O(2n)
        Space Complexity: O(1) ✅ -> (Sorting is done in-place)
"""
def better(nums: list[int]):
    # Count occurrences of 0, 1, and 2
    count_0, count_1, count_2 = 0, 0, 0
    
    for num in nums:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else: 
            count_2 += 1
    
    # Overwrite the original array based on counts
    index = 0
    # Fill the array with `count_0` number of 0s
    for _ in range(count_0):
        nums[index] = 0
        index += 1

    # Fill the array with `count_1` number of 1s
    for _ in range(count_1):
        nums[index] = 1
        index += 1

    # Fill the array with `count_2` number of 2s
    for _ in range(count_2):
        nums[index] = 2
        index += 1
    
    return nums


"""
    Optimal Approach: Two Pointer (Dutch National Flag Alogoritm)
        Time Complexity:  O(N)
        Space Complexity: O(1) ✅ -> (Sorting is done in-place)
"""
def optimal(nums: list[int]):
    """
        Rules:
          - If nums[i] == 0 → Swap with nums[l] and move both `l` and `i` forward.
          - If nums[i] == 2 → Swap with nums[r] and move `r` backward (but don't move `i` to recheck swapped value).
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
            l += 1    # Move forward left pointer 
        # Rule 2
        if (nums[i] == 2):
            # Swap current element with right pointer and move right backward
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1    # Reduce right pointer  
        else:
            i += 1
    
    return nums
    


# Main Function
def sortColors(nums: list[int]) -> None:
    # low, high = 0, len(nums) - 1
    # divide(nums, low, high)
    # better(nums)
    print(optimal(nums))

sortColors([1, 0, 2] * 100000)
sortColors([2, 0, 1])
sortColors([2, 0, 2, 1, 1, 0, 1])
sortColors([1, 1, 1, 0, 1, 1, 1])

"""
    [2, 0, 2, 1, 1, 0]
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
    