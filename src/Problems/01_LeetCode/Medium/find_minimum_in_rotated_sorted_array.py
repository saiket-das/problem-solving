# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/


"""
    Brute Force: Linear Search
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""
def brute_force(nums: list[int]) -> int:
    minimum = float('inf')

    for num in nums:
        if num < minimum:
            minimum = num
        
    return minimum



"""
    Optimal: Binary Search
        Time Complexity:  O(log n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int]) -> int:
    # Get the length of the list
    n = len(nums)

    # Initialize two pointers and minimum value to infinity
    low, high, minimum = 0, n - 1, float('inf')

    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # Update minimum if the current middle element is smaller
        minimum = min(nums[mid], minimum)

        # Check if the left half is sorted
        if nums[low] <= nums[mid]:
            # If the entire segment is sorted, the minimum must be on the left side
            if nums[low] <= nums[high]:
                high = mid - 1
            else:
                low = mid + 1
        # Otherwise, move towards the smaller half
        else:
            high = mid - 1

    return minimum 



def optimal(nums: list[int]) -> int:
    # Get the length of the list
    n = len(nums)

    # Initialize two pointers and minimum value to infinity
    low, high, minimum = 0, n - 1, float('inf')

    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # If the entire segment is sorted, the minimum must be the `low` index element
        if nums[low] <= nums[high]:
            minimum = min(nums[low], minimum)

        # Check if the left half is sorted
        if nums[low] <= nums[mid]:
            minimum = min(nums[low], minimum)
            low = mid + 1
        # Otherwise, move towards the smaller half
        else:
            minimum = min(nums[mid], minimum)
            high = mid - 1

    return minimum 


# Main Function
def findMin(nums: list[int]) -> int:
    # print(brute_force(nums))
    print(optimal(nums))


findMin([2,3,0,1])          # 0
findMin([3,4,5,1,2])        # 1
findMin([11,13,15,17])      # 11
findMin([4,5,6,7,0,1,2])    # 0


"""
   4 5 6 7 0 1 2 (mid = 3)
         m
         
      
"""