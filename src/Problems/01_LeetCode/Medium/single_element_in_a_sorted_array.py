# https://leetcode.com/problems/single-element-in-a-sorted-array/description/


from collections import defaultdict


"""
    Brute Force: HashMap
        Time Complexity:  O(n) + O(n)
        Space Complexity: O(n)
"""
def brute_force(nums: list[int]) -> int:
    freq_dict = defaultdict(int)

    # Find the frequence of all elements 
    for num in nums:
        freq_dict[num] += 1
    
    # Find single frequence element 
    for k, v in freq_dict.items():
        if v == 1:
            return k    # Return single frequence element
        


"""
    Better: Linear Search
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""
def better(nums: list[int]) -> int:
    # Get the length of the List
    n = len(nums)

    # Check if the list has only 1 elements, then return first element 
    if n == 1:
        return nums[0]
    
    # Check if the first element is unique
    if nums[0] != nums[1]:
        return nums[0]
    
    # Check if the last element is unique
    if nums[n - 2] != nums[n - 1]:
        return nums[n - 1]
        
    for i in range(1, n - 2):
        # Check if the number is different from the one before and after it
        if nums[i - 1] != nums[i] and nums[i] != nums[i + 1]:
            return nums[i]    # Return the element if it meets the condition



"""
    Optimal: Binary Search
        Time Complexity:  O(log n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int]) -> int:
    # Get the length of the List
    n = len(nums)

    # If the list has only one element, return it
    if n == 1:
        return nums[0]
    
    # Check if the first element is unique
    if nums[0] != nums[1]:
        return nums[0]
    
    # Check if the last element is unique
    if nums[n - 2] != nums[n - 1]:
        return nums[n - 1]
    
    # Initialize two pointers
    low, high = 1, n - 2

    while low <= high:
        # Calculate mid index
        mid = (low + high) // 2

        # Check if mid is the unique element
        if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        
        # If `mid` is odd and nums[mid - 1] is equal to nums[mid]
        # or `mid` is Even and nums[mid] is equal to nums[mid + 1]
        elif (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
            low = mid + 1     # Unique element lies in the right half
        else:
            high = mid - 1    # Unique element lies in the left half
    
    # If no unique element was found in the loop, return the last element
    return nums[n - 1]
        

# Main Function
def singleNonDuplicate(nums: list[int]) -> int:
    # print(brute_force(nums))
    print(better(nums))
    # print(optimal(nums))



singleNonDuplicate([1])                      # 1
singleNonDuplicate([1,1,2])                  # 2
singleNonDuplicate([1,2,2])                  # 1
singleNonDuplicate([1,1,2,3,3,4,4,8,8])      # 2
singleNonDuplicate([3,3,7,7,10,11,11])       # 10
singleNonDuplicate([7,7,10,11,11,12,12])     # 10

"""
    Optimal Approach
    -----------------
    -----------------
    Thought Process
    -----------------
    0 1 2 3 4 5 6
    -----------------
    3 3 7 7 8 9 9
    E O E O E O E
           ---
    -----------------
    0 1 2 3 4 5 6 7 8
    -----------------
    1 1 2 3 3 4 4 8 8
    E O E O E O E O E
       ---
    ----------------
    1. (Even, Odd) -> Left half (Element is in right half)
        Means if `mid` index is Odd number then eliminate left half
    2. (Odd, Even) -> Right half (Element is in the Left half)
        Means if `mid` index is Even number then eliminate right half
"""