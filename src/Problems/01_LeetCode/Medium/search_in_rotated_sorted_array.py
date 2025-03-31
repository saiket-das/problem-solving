# https://leetcode.com/problems/search-in-rotated-sorted-array/description/


"""
    Brute Force: Linear Search
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""
def brute_force(nums: list[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num == target:
            return i
    
    return -1 



"""
    Optimal: Binary Search
        Time Complexity:  O(log n)
        Space Complexity: O(1)
    
    Steps:
      - Determine which half is Sorted
      - Determine `target` lies on which half (sorted or unsorted half)
"""
def optimal(nums: list[int], target: int) -> int:
    # Get the length of the list
    n = len(nums)

    # Set up two pointers for binary search
    low, high = 0, n - 1

    # Perform binary search
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # If the target is found, return its index
        if nums[mid] == target:
            return mid
        
        # Determine which half is sorted
        if nums[low] <= nums[mid]:    # Left half is sorted
            if nums[low] <= target and target <= nums[mid]:
                # Target lies within the sorted left half
                high = mid - 1
            else:
                # Target is in the right half
                low = mid + 1

        else:    # Right half is sorted
            if nums[mid] <= target and target <= nums[high]:
                # Target lies within the sorted right half
                low = mid + 1
            else:
                # Target is in the left half
                high = mid - 1
    
    # If the target is not found, return -1
    return -1




        

# Main Function
def search(nums: list[int], target: int) -> int:
    # print(brute_force(nums, target))
    print(optimal(nums, target))


search([1], 0)                # -1
search([4,5,6,7,0,1,2], 0)    # 4
search([4,5,6,7,0,1,2], 3)    # -1