# https://leetcode.com/problems/find-peak-element/description/


"""
    Brute Force: Linear Search
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""
def brute_force(nums: list[int]) -> int:
    # Get the length of list
    n = len(nums)

    # If the list has only one element, the peak is at index 0
    if n == 1:
        return 0
    
    # Initialize peak index to 0
    peak = 0

    # Iterate through the list from second element to second-last element
    for i in range(1, n - 1):
        # Check if the current element is greater than both its neighbors
        if nums[i - 1] < nums[i] > nums[i + 1]:
            peak = i    # Update peak index to the current position

    # Return the peak index if it's greater than the last element, otherwise return the last index
    return peak if nums[peak] > nums[n - 1] else n - 1



"""
    Optimal: Binary Search
        Time Complexity:  O(log n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int]) -> int:
    # Get the length of list
    n = len(nums)

    # If the list has only one element, the peak is at index 0
    if n == 1:
        return 0
    
    # Check if the first element is a peak (greater than the second element)
    if nums[0] > nums[1]:
        return 0
    
    # Check if the last element is a peak (greater than the second-last element)
    if nums[n - 2] < nums[n - 1]:
        return n - 1
    
    # Initialize `peak` index and two pointers for binary search
    peak, low, high = 1, 1, n - 2

    # Perform binary search to find a peak element
    while low <= high:
        mid = (low + high) // 2

        # If mid element is greater than both neighbors, it's a peak
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid    # Found a peak, return its index
        
        # If mid element is part of an increasing sequence, move right
        elif nums[mid - 1] < nums[mid] <  nums[mid + 1]:
            low = mid + 1
        
        # If mid element is part of a decreasing sequence, move left
        else:
            high = mid - 1
        
    # Return the peak index
    return peak


# Main function
def findPeakElement(nums: list[int]) -> int:
    # print(brute_force(nums))
    print(optimal(nums))

findPeakElement([2,1])              # 0
findPeakElement([1,2])              # 1
findPeakElement([1,2,3,1])          # 2
findPeakElement([1,0,0,0])          # 0
findPeakElement([0,0,0,1])          # 3
findPeakElement([0,1,2,1])          # 2
findPeakElement([2,1,2,0])          # Either 0 or 2
findPeakElement([1,2,5,3,4,6,4])    # Either 2 or 5