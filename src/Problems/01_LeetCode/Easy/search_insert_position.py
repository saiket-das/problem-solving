# https://leetcode.com/problems/search-insert-position/description/


"""
    Optimal: Binary Search
        Time Complexity:  O(log n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int], target: int) -> int:
    # Get the length of the list
    n = len(nums)

    # Initialize binary search boundaries
    left, right = 0, n - 1

    while left <= right:
        # Find mid index
        mid = (left + right) // 2
        
        # Target found, return index
        if nums[mid] == target:
            return mid  
        # Search in the right half
        elif nums[mid] < target:
            left = mid + 1
        # Search in the left half
        else:
            right = mid - 1
    
    # `left` is the insert position (where target should be placed)
    return left

def searchInsert(nums: list[int], target: int) -> int:
    print(optimal(nums, target))


searchInsert([1,3,5,6], 5)    # 2
searchInsert([1,3,5,6], 2)    # 1
searchInsert([1,3,5,6], 7)    # 4