# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


"""
    Brute Force: Linear Search
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""
def brute_force(nums: list[int], target: int) -> list[int]:
    # Initialize answer with default values
    ans = [-1, -1]

    for i, num in enumerate(nums):
        if num == target:
            if ans[0] == -1 and ans[1] == -1:
                ans[0] = ans[1] = i    # Store first and second occurrence
                continue
            else:
                ans[1] = i
        
        # If both occurrences are found, return early
        if ans[0] != -1 and ans[1] != -1:
            return ans
    
    return ans

"""
    Optimal: Binary Search (Lower bound and Upper bound)
        Time Complexity:  2 * O(log n)
        Space Complexity: O(1)
"""
def lower_bound(nums: list[int], target: int) -> list[int]:
    # Get the length of the list
    n = len(nums)
    
    # Set up two pointers for binary search
    low, high = 0, n - 1

    # Initialize the lower bound with default values -1
    ans = n

    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # maybe an answer
        if nums[mid] >= target:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    
    return ans

def upper_bound(nums: list[int], target: int) -> list[int]:
    # Get the length of the list
    n = len(nums)
    
    # Set up two pointers for binary search
    low, high = 0, n - 1

    # Initialize the lower bound with default values -1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    # Return [-1, -1] if the target is not found
    return ans

def optimal(nums: list[int], target: int) -> list[int]:
    # Find the first position where 'target' should be inserted (lower bound)
    lb = lower_bound(nums, target)

    # Find the first position where an element > 'target' should be inserted (upper bound)
    up = upper_bound(nums, target) - 1

    # If 'target' is not in 'nums' (either out of bounds or not an exact match)
    if lb == len(nums) or nums[lb] != target:
        return [-1, -1]     # Target not found

    return [lb, up]
     


"""
    Optimal 2: Binary Search
        Time Complexity:  O(log n)
        Space Complexity: O(1)
"""
def optimal_2(nums: list[int], target: int) -> list[int]:
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
        return ans
    
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
    
    return ans


def searchRange(nums: list[int], target: int) -> list[int]:
    # print(brute_force(nums, target))
    # print(optimal(nums, target))
    print(optimal_2(nums, target))


searchRange([], 0)                  # [-1, -1]
searchRange([1], 1)                 # [0, 0]
searchRange([5,7,7,8,8,10], 8)      # [3, 4]
searchRange([5,7,7,8,8,10], 6)      # [-1, -1]
searchRange([1,1,1,2,3,4,5], 1)     # [0, 2]
searchRange([1,1,2,3,4,5], 2)       # [2, 2]