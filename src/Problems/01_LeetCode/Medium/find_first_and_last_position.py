# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/



"""
    Optimal: Binary Search
        Time Complexity:  O(log n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int], target: int) -> list[int]:
    # Get the length of the list
    n = len(nums)

    # Initialize the result with default values (-1, -1) meaning "not found"
    ans = [-1, -1]

    # If the array has less than 2 elements, return the default result
    if n < 1:
        return ans
    
    # Set up two pointers for binary search
    left, right, idx = 0, n - 1, 0

    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            # Store the first found index
            ans[idx] = mid
            idx += 1
        
        # Move right if target is greater
        elif nums[mid] < target:
            left = mid + 1
        # Move left if target is smaller
        else:
            right = mid - 1
    
    # Return [-1, -1] if the target is not found
    return ans 
    


def searchRange(nums: list[int], target: int) -> list[int]:
    print(optimal(nums, target))



searchRange([], 0)                # [-1, -1]
searchRange([1], 1)               # [-1, -1]
searchRange([5,7,7,8,8,10], 8)    # [3, 4]
searchRange([5,7,7,8,8,10], 6)    # [-1, -1]
searchRange([1,1,2,3,4,5], 1)     # [0, -1]
searchRange([1,1,2,3,4,5], 2)     # [0, -1]