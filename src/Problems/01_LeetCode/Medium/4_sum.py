# https://leetcode.com/problems/4sum/description/

from collections import defaultdict

"""
    Brute Force: Nested Loop 
        Time Complexity:  O(n^4 * log(m))
        Space Complexity: 2 * O(m) 

        `n` = The length of nums list & `m` = The length of unique_quadruplet
"""
def brute_force(nums: list[int], target: int) -> list[list[int]]:
    # Get the length of list
    n = len(nums)

    # Use a set to store unique quadruplets (avoiding duplicate results)
    unique_quadruplet = set([])

    # Iterate through all possible quadruplet combinations
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    # Calculate the sum of the selected four numbers
                    four_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    # If the sum matches the target, store the quadruplet
                    if four_sum == target:
                        # Sort and convert to a tuple to ensure uniqueness
                        quadruplet = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                        unique_quadruplet.add(quadruplet)
            
    # Convert each tuple back to a list before returning the result
    return [list(quadruplet) for quadruplet in unique_quadruplet]


"""
    Better: Nested Loop + Set
        Time Complexity:  O(n^3 * log(m))
        Space Complexity: O(n) + 2 * O(p)

        `n` = The length of nums list & `m` = The length of set & `p` = The length of unique_quadruplets 
"""
def better(nums: list[int], target: int) -> list[list[int]]:
    n = len(nums)

    # Use a set to store unique quadruplets (avoiding duplicate results)
    unique_quadruplets = set()

    # Iterate through all possible quadruplet combinations
    for i in range(n):
        for j in range(i + 1, n):
            # Use a set to track elements seen so far in the current iteration
            hashSet = set()

            # Iterate through the remaining elements (k)
            for k in range(j + 1, n):
                # Calculate the required fourth number to reach the target sum
                fourth = target - (nums[i] + nums[j] + nums[k])

                # If the required number is already seen, a valid quadruplet is found
                if fourth in hashSet:
                    # Sort and store the quadruplet as a tuple to ensure uniqueness
                    quadruplet = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
                    unique_quadruplets.add(quadruplet)
                
                # Add the current element to the hash set for future lookups
                hashSet.add(nums[k])
            
    # Convert each tuple back to a list before returning the result
    return [list(quadruplet) for quadruplet in unique_quadruplets]


"""
    Optimal: Nested Loop + Set
        Time Complexity:  O(n log n) + O(n^3) 
        Space Complexity: O(m)

        `n` = The length of nums list & `m` = The length of unique_quadruplets 
"""
def optimal(nums: list[int], target: int) -> list[list[int]]:
    # Sort the array to facilitate two-pointer approach and avoid duplicates
    nums.sort()

    # Get the length of the list
    n = len(nums)

    # Store unique quadruplets (avoiding duplicate results)
    unique_quadruplets = []
    
    # Iterate through all possible first elements of the quadruplet
    for i in range(n):
        # Skip duplicate values for the first element to avoid duplicate quadruplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):
            # Skip duplicate values for the second element to avoid duplicate quadruplets
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # Initialize two pointers for the remaining two numbers
            left, right = j + 1, n - 1

            while left < right:
                # Calculate the sum of the four numbers
                four_sum = nums[i] + nums[j] + nums[left] + nums[right]

                # Increase sum by moving the left pointer forward
                if four_sum < target:
                    left += 1     
                # Decrease sum by moving the right pointer backward
                elif four_sum > target:
                    right -= 1    
                else:
                    # Found a valid quadruplet
                    quadruplet = [nums[i], nums[j], nums[left], nums[right]]
                    unique_quadruplets.append(quadruplet)
                    # Move both pointers to find the next unique quadruplet
                    left += 1
                    right -= 1

                    # Skip duplicate values for the third element to avoid duplicate results
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while  left < right and nums[right] == nums[left + 1]:
                        right -= 1

    return unique_quadruplets



# Main Function
def fourSum(nums: list[int], target: int) -> list[list[int]]:
    # print(brute_force(nums, target))
    # print(better(nums, target))
    print(optimal(nums, target))


fourSum([0,0,0,0], 2)               # []
fourSum([0,0,0,0], 0)               # [0,0,0,0]
fourSum([2,2,2,2,2], 8)             # [[2,2,2,2]]
fourSum([2,2,2,2,2,0,2,4], 8)       # [[2,2,2,2]]
fourSum([1,0,-1,0,-2,2], 0)         # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
fourSum([-1,0,-10,10,2,3,5], 20)    # [0,0,0,0]
fourSum([1,-2,-5,-4,-3,3,3,5], -11)    # [0,0,0,0]