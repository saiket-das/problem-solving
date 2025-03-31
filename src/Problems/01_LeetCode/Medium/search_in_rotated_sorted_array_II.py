# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/



"""
    Brute Force: Linear Search
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""
def brute_force(nums: list[int], target: int) -> bool:
    for num in nums:
        if num == target:
            return True
    
    return False


"""
    Optimal: Binary Search
        Time Complexity:  O(n)
        Space Complexity: O(1)
    
    
"""
def optimal(nums: list[int], target: int) -> bool:
    # Get the length of the list
    n = len(nums)

    # Initialize two pointers
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        # Found the target value
        if nums[mid] == target:
            return True
        
        # Handle the edge case where duplicates exist at both ends
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue  # Skip the current iteration to avoid ambiguity

        # Determine which half is Sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target <= nums[mid]:
                # Target lies within the sorted left half
                high = mid - 1
            else:
                # Target is in the right half
                low = mid + 1
        else:
            if nums[mid] <= target and target <= nums[high]:
                # Target lies within the sorted right half
                low = mid + 1
            else:
                # Target is in the left half
                high = mid - 1
    
    # If target is not found, return False
    return False


def search(nums: list[int], target: int) -> bool:
    # print(brute_force(nums, target))
    print(optimal(nums, target))


search([2,5,6,0,0,1,2], 0)     # True
search([2,5,6,0,0,1,2], 3)     # False
search([3,3,1,2,3,3,3,3], 2)    # True (Edge case) -> nums[l] == nums[m] == nums[h]
search([3,3,1,3,3,3,3,3], 3)    # True (Edge case) -> nums[l] == nums[m] == nums[h]