# https://leetcode.com/problems/majority-element-ii/description/

from collections import defaultdict


"""
    Brute Force: Nested Loop
        Time Complexity:  O(n * n)
        Space Complexity: O(2)
"""
def brute_force(nums: list[int]) -> list[int]:
    # Get the length of the input list
    n = len(nums)

    # Use a set (avoid duplicates) to store elements appearing more than n // 3 times
    result: list[int] = [] * 2    # SC: O(2)

    # Iterate over each element in the list
    for i in range(n):
        # Skip if the number is already processed
        if nums[i] in result:
            continue

        # Initialize count for the current element
        count = 1
        # Count occurrences of nums[i] in the list
        for j in range(n):
            if nums[i] == nums[j] and i != j:    # Avoid counting itself
                count += 1
        
        # If the count exceeds n // 3, add to the result set
        if count > n // 3:
            result.append(nums[i])
        
        if len(result) == 2:
            break
    
    # Convert the set to a list before returning
    return result


"""
    Better: HashMap
        Time Complexity:  O(n)
        Space Complexity: O(n + 2)
"""
def better(nums: list[int]) -> list[int]:
    # Get the length of the input list
    n = len(nums)

    # Dictionary to count the frequency of each numbe
    # List to store numbers that appear more than n // 3 times
    freq_map = defaultdict(int)    # SC: O(n)
    result = set()                 # SC: O(2)

    # Count occurrences of each number
    for num in nums:
        freq_map[num] += 1
        # Check if the count exceeds n // 3
        if freq_map[num] > n // 3:
            result.add(num)
        
        # If the length of result is 2, then break the loop 
        if len(result) == 2:
            break
        
    return list(result)


"""
    Optimal: Boyer-Moore Voting Algorithm
        Time Complexity:  O(n + n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int]) -> list[int]:
    # Get the length of the input list
    n = len(nums)

    # Initialize two potential majority element candidates and their respective counts
    count_1, count_2 = 0, 0
    ele_1, ele_2 = float('-inf'), float('-inf')

    # Find potential majority elements
    for num in nums:
        # Assign new candidate to ele_1
        if count_1 == 0 and num != ele_2:
            count_1, ele_1 = 1, num
        # Assign new candidate to ele_2
        elif count_2 == 0 and num != ele_1:
            count_2, ele_2 = 1, num
        # Increment count if num matches first candidate
        elif ele_1 == num :
            count_1 += 1
        # Increment count if num matches second candidate
        elif ele_2 == num :
            count_2 += 1
        # Reduce counts when a different number is encountered
        else:
            count_1 -=1
            count_2 -= 1
    
    # Verify the candidates by counting their occurrences
    count_1, count_2 = 0, 0
    for num in nums:
        if ele_1 == num:
            count_1 += 1
        if ele_2 == num:
            count_2 += 1
    
    # Check if the both count exceeds n // 3
    result = []
    if count_1 > n // 3:
        result.append(ele_1)
    if count_2 > n // 3:
        result.append(ele_2)
    
    # Return sorted result
    return sorted(result)
 

# Main function
def majorityElement(nums: list[int]) -> list[int]:
    # print(brute_force(nums))
    # print(better(nums)) 
    print(optimal(nums))

 
majorityElement([1])                # [1]
majorityElement([2,2])              # [2]
majorityElement([3,2,3])            # [3]
majorityElement([1,2])              # [1,2]
majorityElement([3,3,2,2,2,3,1])    # [2,3]
majorityElement([1,3,3,3,3,1,2,1])  # [1,3]