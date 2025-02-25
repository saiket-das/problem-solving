# https://leetcode.com/problems/binary-search/description/


"""
    Time Complexity:  O(log n)
    Space Complexity: O(1)
"""

def search(nums: list[int], target: int) -> int:
    # Initialize two pointers (left and right) for binary search
    l, r = 0, len(nums) - 1

    while (l <= r):
        # Find the middle index
        mid = (l + r) // 2

        # If mid element is the target, return the index
        if (nums[mid] == target):
            return mid
        
        # If target is greater, search the right half
        if (nums[mid] < target):
            l = mid + 1
        # If target is smaller, search the left half
        else:
            r = mid - 1
            
    # Target not found
    return -1

print(search([-1,0,3,5,9,12], 2))

"""
    Target TC: O(log n)
"""

"""
    -----------
    Example 1:
        Input: nums = [-1,0,3,5,9,12], target = 9
        Output: 4
        Explanation: 9 exists in nums and its index is 4
    -----------
    Example 2:
        Input: nums = [-1,0,3,5,9,12], target = 2
        Output: -1
        Explanation: 2 does not exist in nums so return -1
    -----------
"""