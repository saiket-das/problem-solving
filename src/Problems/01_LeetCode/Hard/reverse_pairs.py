# https://leetcode.com/problems/reverse-pairs/description/

"""
    Brute Force: Nested Loop 
        Time Complexity:  O(n^2) -> (Time limit exceeded)
        Space Complexity: O(1)
"""
def brute_force(nums: list[int]) -> int:
    # Get the length of the input list
    n = len(nums)

    # Initialize counter for valid pairs
    count = 0

    # Iterate through each element in the list
    for i in range(n):
        for j in range(i, n):
            # Check if nums[i] is more than twice nums[j] (nums[i] > 2 * nums[j])
            if nums[i] > 2 * nums[j]:
                count += 1    # Increment
    
    return count



"""
    Optimal: Merge Sort 
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
"""
# Divide
def divide(nums, low, high):
    count = 0
    if low >= high:    # Base Case
        return count
    
    # Find `mid`
    mid = (low + high) // 2

    # Divide the list
    count += divide(nums, low, mid)
    count += divide(nums, mid + 1, high)

    count += count_pairs(nums, low, mid, high)
    # Merge the divided list
    conquer(nums, low, mid, high)

    return count

# Merge two sorted halves of the list `nums` in place
def conquer(nums, low, mid, high):
    # Pointers to track left and right subarrays
    left, right = low, mid + 1

    # Temporary list to store sorted elements
    temp = []
    # Merge elements from both halves in sorted order
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            # If left element is smaller, add it first
            temp.append(nums[left])
            left += 1
        else:
            # Otherwise, add the right element first
            temp.append(nums[right])
            right += 1
    
    # Copy remaining elements from the left half (if any)
    while left <= mid:
        temp.append(nums[left])
        left += 1
    
    # Copy remaining elements from the right half (if any)
    while right <= high:
        temp.append(nums[right])
        right += 1

    # Copy sorted elements from `temp` back to `nums` in the original range
    for i in range(low, high + 1):
        nums[i] = temp[i - low]

# Count the reverse pairs
def count_pairs(nums, low, mid, high):
    right = mid + 1
    count = 0
    for i in range(low, mid + 1):
        while right <= high and nums[i] > 2 * nums[right]:
            right += 1
        count += (right - (mid + 1))
        
    return count

def optimal(nums: list[int]) -> int:
    # Get the length of the input list
    n = len(nums)
    # Count reverse pairs using Merge Sort
    count = divide(nums, 0, n - 1)
    
    return count



# Main Function
def reversePairs(nums: list[int]) -> int:
    # print(brute_force(nums))
    print(optimal(nums))

reversePairs([1] * 10000)    # 0
reversePairs([1,3,2,3,1])    # 2
reversePairs([2,4,3,5,1])    # 3


"""
    A reverse pair is a pair (i, j) where:
      - 0 <= i < j < nums.length and
      - nums[i] > 2 * nums[j]
"""