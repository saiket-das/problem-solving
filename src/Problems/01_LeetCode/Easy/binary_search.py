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


print(search([-1,0,3,5,9,12], 5))


def recursion(arr, low, high, target) -> list[int]:
    if (low > high):    # Base Case
        return - 1
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursion(arr, mid + 1, high, target)
    else:
        return recursion(arr, low, mid - 1, target)


def binary_search_recursion(arr, target) -> list[int]:
    n = len(arr)
    low, high = 0, n - 1

    idx = recursion(arr, low, high, target)
    return idx


print(binary_search_recursion([-1,0,3,5,9,12], 12))

"""
    Target TC: O(log n)
"""
