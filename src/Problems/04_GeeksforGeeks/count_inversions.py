# https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=inversion-of-array


"""
    Brute Force: Nested Loop
        Time Complexity:  O(n^2)
        Space Complexity: O(1)
"""
def brute_force(nums):
    # Get the length of the list
    n = len(nums)

    # Initialize counter for valid pairs
    count = 0

    # Iterate through each element in the list
    for i in range(n):
        for j in range(i, n):
            # If a later element is smaller, increment the count
            if nums[j] < nums[i]:
                count += 1
    
    # Return the total count of valid pairs 
    return count



"""
    Optimal: Merge Sort
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
"""
def divide(nums, low, high):
    counter = 0
    if low >= high:
        return counter
    mid = (low + high) // 2
    # Divide the list
    counter += divide(nums, low, mid)
    counter += divide(nums, mid + 1, high)
    # Merge the divided list
    counter += conquer(nums, low, mid, high)

    return counter

def conquer(nums, low, mid, high):
    temp = []
    left, right = low, mid + 1

    # Initialize counter for valid pairs
    counter = 0

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            counter += (mid - left + 1)    # Answer
            right += 1
    
    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= high:
        temp.append(nums[right])
        right += 1
    
    # Copy sorted elements from `temp` back to `nums` in the original range
    for i in range(low, high + 1):
        nums[i] = temp[i - low]

    return counter


def optimal(nums):
    n = len(nums) 

    # Merge sort
    counter = divide(nums, 0, n - 1)
    print(nums)
    
    # Return the total count of valid pairs 
    return counter


# Main Function
def inversionCount(nums):
    # print(brute_force(nums))
    print(optimal(nums))

inversionCount([10, 10, 10])       # 0
inversionCount([2, 3, 4, 5, 6])    # 0
inversionCount([2, 4, 1, 3, 5])    # 3 => [(2, 1), (4, 1), (4, 3)]