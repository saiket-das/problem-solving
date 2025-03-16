# https://leetcode.com/problems/3sum/description/

from collections import defaultdict

"""
    Brute Force: Nested Loop 
        Time Complexity:  O(n^3 * log(m))
        Space Complexity: 2 * O(m) 

        `n` = The length of nums list & `m` = The length of unique_triplets
"""
def brute_force(nums: list[int]) -> list[list[int]]:
    # Get the length of the nums list
    n = len(nums)

    # Use a set to store unique triplets
    unique_triplets = set()  

    # Iterate through all possible triplet combinations
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + i, n):
                # Calculate the sum of the triplet
                three_sum = nums[i] + nums[j] + nums[k]
                
                # Check if the sum equals zero
                if three_sum == 0 :
                    # Sort to avoid duplicate sets
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))    # SC: O(3 log 3) -> O(1)
                    unique_triplets.add(triplet)
    
    # Convert back to list format
    return [list(triplet) for triplet in unique_triplets]



"""
    Better: Nested Loop 
        Time Complexity:  O(n^2) * O(log s) => O(n^2)
        Space Complexity: O(n) + O(m) * 2

        `n` = The length of nums list & `m` = The length of unique_triplets & `s` = The length of hashSet 
"""
def better(nums: list[int]) -> list[list[int]]:
    # Get the length of the nums list
    n = len(nums)

    # Use a set to store unique triplets (to avoid duplicates)
    unique_triplets = set()

    # Iterate through the list, considering each element as the first number of a triplet
    for i in range(n):
        # A hashset to track elements for quick lookup of the third number
        hashset = set()

        # Iterate through the remaining elements to find valid pairs
        for j in range(i + 1, n):
            # Calculate the required third number to form a zero sum
            third_element = -(nums[i] + nums[j])

            # If the third element is already in the hashset, a valid triplet is found
            if third_element in hashset:
                # Sort to maintain uniqueness
                triplet = tuple(sorted([nums[i], nums[j], third_element]))
                # Add the triplet to the set
                unique_triplets.add(triplet)
            
            # Add the current number to the hashset for future lookups
            hashset.add(nums[j])
    
    # Convert the set of tuples back to a list of lists and return
    return [list(triplet) for triplet in unique_triplets]
    


"""
    Optimal: Sorting + Two Pointer
        Time Complexity:  O(n log n) + O(n^2)
        Space Complexity: O(1) 
    
    Approach
        1. ** Sorting the array **  
           - Sorting helps in avoiding duplicate triplets efficiently.
           - It also allows using the **Two-Pointer Technique**.
    
        2. ** Iterating through the array **  
           - If `nums[i] > 0`, break the loop (as positive numbers can't sum to zero).
           - If `nums[i]` is a duplicate (`nums[i] == nums[i-1]`), **skip** to avoid duplicate triplets.
    
        3. ** Two-Pointer Technique **  
           - Use `l` (left pointer) and `r` (right pointer) to find a triplet.
           - Compute `three_sum = nums[i] + nums[l] + nums[r]`:
              - If `three_sum < 0`, **increase left** (`l += 1`).
              - If `three_sum > 0`, **decrease right** (`r -= 1`).
              - If `three_sum == 0`, **store triplet and update pointers**.
              - Skip duplicates to avoid redundant triplets.
"""
def optimal(nums: list[int]) -> list[list[int]]:
    # Sort the list
    nums.sort()

    result = []

    # Iterate through the list
    for i, num in enumerate(nums):
         # Since the array is sorted, if num > 0, there can't be a sum of zero
        if num > 0:
            break
        
        # Skip duplicate elements to avoid repeated triplets
        if i > 0 and num == nums[i - 1]:
            continue

       # Initialize two pointers for the two-sum approach
        left, right = i + 1, len(nums) - 1

        while left < right:
            # Calculate Three sum
            three_sum = num + nums[left] + nums[right]

            # Increase left pointer to get a larger sum
            if three_sum < 0:
                left += 1
            # Decrease right pointer to get a smaller sum
            elif three_sum > 0:
                right -=1
            # Valid triplet found, add it to the result
            else:
                result.append([num, nums[left], nums[right]])
                left += 1
                right -=1 
                # Avoid duplicate triplets by skipping repeated elements
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return result



# Main function
def threeSum(nums: list[int]) -> list[list[int]]:
    # print(brute_force(nums))
    # print(better(nums))
    print(optimal(nums))

    
threeSum([0,1,1])                  # []
threeSum([0,0,0])                  # [0]
threeSum([-1,0,1,0])               # [-1, 0, 1]
threeSum([-1, 0, 1, 2, -1, -4])    # [[-1,-1,2],[-1,0,1]]



"""
    ** Notice that the solution set must not contain duplicate triplets. ❌ ** 
"""