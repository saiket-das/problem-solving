# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-occurrence


"""
    Optimal: Binary Search
        Time Complexity:  O(log n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int], target: int) -> list[int]:
    # Get the length of the list
    n = len(nums)
    
    # Set up two pointers for binary search
    low, high = 0, n - 1

    # Initialize the answer list with default values [-1, -1]
    ans = [-1, -1]

    # Binary search to find the first occurrence of target
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            ans[0] = mid       # Update first occurrence
            high = mid - 1     # Continue searching in the left half
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    if ans[0] == -1:
        return 0
    
    # Reset pointers for the second search
    low, high = 0, n - 1

    # Binary search to find the last occurrence of target
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            ans[1] = mid      # Update last occurrence
            low = mid + 1     # Continue searching in the right half
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return ans[1] - ans[0] + 1


def countFreq(arr: list, target: int) -> int:
    print(optimal(arr, target))


countFreq([1, 1, 2, 2, 2, 2, 3], 2)      # 4 (5 - 2)
countFreq([1, 1, 2, 2, 2, 2, 3], 4)      # 0
countFreq([8, 9, 10, 12, 12, 12], 12)    # 3