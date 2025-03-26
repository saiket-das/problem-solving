# https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-missing-and-repeating

from collections import defaultdict


"""
    Brute Force: Nested Loop
        Time Complexity:  O(n^2)
        Space Complexity: O(1)
"""
def brute_force(nums):
    # Get the length of list
    n = len(nums)

    # Initialize variables
    duplicate_number, missing_number = -1, -1

    # Iterate through numbers from 1 to n
    for i in range(n):
        # Count occurrences of the current number
        count = 0
        # Check how many times (i+1) appears in the array
        for j in range(n):
            if nums[j] == i + 1:
                count += 1
        
        # Identify the duplicate and missing numbers based on count
        if count == 2:
            duplicate_number = i + 1    # Number appears twice
        elif count == 0:
            missing_number = i + 1      # Number is missing
        
        # If both values are found, exit early
        if duplicate_number != -1 and missing_number != -1:
            break
        
    return [duplicate_number, missing_number]
  

"""
    Better: Hashmap 
        Time Complexity:  O(n) + O(n) => O(n)
        Space Complexity: O(n)
"""
def better(nums):
    # Get the length of list
    n = len(nums)

    # Create a frequency dictionary to count occurrences of each number
    freq_dict = defaultdict(int)
    for num in nums:
        freq_dict[num] += 1
    
    # Initialize variables
    duplicate_number, missing_number = -1, -1
    # Identify the duplicate and missing number
    for i in range(1, n + 1):
        if freq_dict[i] == 2:
            duplicate_number = i
        elif freq_dict[i] == 0:
            missing_number = i
        
        if duplicate_number != -1 and missing_number != -1:
            break

    return [duplicate_number, missing_number]
    

"""
    Optimal 1: Math 
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""
def optimal(nums):
    n = len(nums)

    # Actual sum and Actual square sum
    actual_sum, actual_square_sum = 0, 0
    for num in nums:
        actual_sum += num
        actual_square_sum += (num ** 2)
    
    # Expected sum => Formula: (n * (n + 1) // 2)
    expected_sum = (n * (n + 1)) // 2
    # Find (x - y = i1)
    i1 = actual_sum - expected_sum

    # Expected sum ^2 => Formula: (n *  (n + 1) * (2n + 1)) / 6
    expected_square_sum = (n * (n + 1) * (2*n + 1)) // 6

    # Find (x^2 - y^2 = i2) 
    i2 = actual_square_sum - expected_square_sum
    
    #  Find (x + y = i3)
    i3 = i2 // i1

    # (x + y) (x - y) = i2 (Find x)
    duplicate_number = (i1 + i3) // 2
    # (x + y) (x - y) = i2 (Find y)
    missing_number = i3 - duplicate_number

    return [duplicate_number, missing_number]


"""
    Optimal: XOR 
        Time Complexity:  O(n) + O(n) + O(n) + O(n) => O(n)
        Space Complexity: O(1)
"""
def optimal_2(nums):
    n = len(nums)

    xor = 0
    for i, num in enumerate(nums):
        xor ^= num
        xor ^= (i + 1)
    
    bit_num = 0
    while 1:
        if (xor & (1 << bit_num)) != 0:
            break
        bit_num += 1

    zero, one = 0, 0
    for num in nums:
        # Part of `ONE` club
        if (num & (1 << bit_num)) != 0:
            one ^= num
        # Part of `ZERO` club
        else:
            zero ^= num
    
    for num in range(1, n + 1):
        # Part of `ONE` club
        if (num & (1 << bit_num)) != 0:
            one ^= num
        # Part of `ZERO` club
        else:
            zero ^= num
    
    count = 0
    for num in nums:
        if num == zero:
            count += 1
    
    
    return [zero, one] if count == 2 else [one, zero]



# Main Function
def findTwoElement(nums): 
    # print(brute_force(nums))
    # print(better(nums))
    # print(optimal(nums))
    print(optimal_2(nums))


findTwoElement([2, 2])                # [2, 1] -> 2 = Duplicate, 1 = Missing
findTwoElement([1, 3, 3] )            # [3, 2]
findTwoElement([4, 3, 6, 2, 1, 1])    # [1, 5]