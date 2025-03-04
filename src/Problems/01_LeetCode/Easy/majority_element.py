# https://leetcode.com/problems/majority-element/description/

from collections import defaultdict

"""
    Brute Force Approach: Nested Loop
        Time Complexity:  O(N^2)
        Space Complexity: O(1)
"""
def brute_force(nums: list[int]) -> int:
    n: int = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] == nums[j]:
                count += 1
        if count > (n // 2):
            return nums[i]


"""
    Better Approach: Hashmap
        Time Complexity:  O(N) + O(N) => O(N)
        Space Complexity: O(N)
"""
def better(nums: list[int]) -> int:
    # Dictionary to store element frequencies
    freq_dict = defaultdict(int)    # SC: O(N)

    # Count occurrences of each number
    for num in nums:    # TC: O(N)
        freq_dict[num] += 1
    
    # Find the Element with the Maximum Frequency and Return
    return max(freq_dict, key=freq_dict.get)    # TC: O(N)



"""
    ----------------
    Optimal Approach
    ----------------
    Thought Process:

    The goal is to find the majority element (the element that appears more than ⌊n / 2⌋ times).
    We use **Boyer-Moore Voting Algorithm**, which works in two phases:
    
    1. **Candidate Selection Phase**:
        - We iterate through the array while maintaining a candidate element and a count.
        - If `count = 0`, we assume the current element as the new candidate.
        - If the current element matches the candidate, we increment the count.
        - Otherwise, we decrement the count.

    2. **Candidate Verification Phase (Optional for guaranteed majority element)**:
        - In problems where a majority element is **not guaranteed**, we need an extra loop to verify 
          that the selected candidate actually occurs more than ⌊n / 2⌋ times.

    **Example Execution:**
      Input: [2, 2, 1, 1, 1, 2, 2, 4, 2, 2, 4, 1, 2, 2, 1]
      Expected Output: 2 (appears 8 times, more than 15 / 2 = 7.5)

      Steps:
      - Initialize: `curr_ele = nums[0] (2)`, `count = 1`
      - Iterate through `nums`:
          - nums[1] = 2 → count++ (count = 2)
          - nums[2] = 1 → count-- (count = 1)
          - nums[3] = 1 → count-- (count = 0) → Reset `curr_ele = nums[4] (1)`, count = 1
          - nums[5] = 2 → count-- (count = 0) → Reset `curr_ele = nums[6] (2)`, count = 1
          - nums[7] = 4 → count-- (count = 0) → Reset `curr_ele = nums[8] (2)`, count = 1
          - nums[9] = 2 → count++ (count = 2)
          - nums[10] = 4 → count-- (count = 1)
          - nums[11] = 1 → count-- (count = 0) → Reset `curr_ele = nums[12] (2)`, count = 1
          - nums[13] = 2 → count++ (count = 2)
          - nums[14] = 1 → count-- (count = 1)

      Final candidate: `2`
      Since we assume the problem guarantees a majority element, we return `curr_ele = 2`.
"""
"""
    Optimal Approach: 
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""
def optimal(nums: list[int]) -> int:
    # Initialize the first element as the candidate and set count to 1
    curr_ele, count = nums[0], 1

    # Iterate through the array to find the majority candidate
    for num in nums:
        # Increase count if the current number matches the candidate
        if curr_ele == num:
            count += 1
        # Decrease count otherwise
        else:
            count -= 1
            # If count reaches zero, choose a new candidate
            if count == 0:
                curr_ele = num
                count = 1

    # Since we assume there is always a majority element, return the candidate
    return curr_ele


# Main Function
def majorityElement(nums: list[int]) -> int:
    # print(brute_force(nums))
    # print(better(nums))
    print(optimal(nums))
    

majorityElement([6, 5, 5])
majorityElement([3, 2, 3])
majorityElement([2, 2, 1, 1, 1, 2, 2])
majorityElement([2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1])


"""
    ** Follow-up: Could you solve the problem in linear time and in O(1) space? **
    -----------
    Example 1:
        Input: nums = [3, 2, 3]
        Output: 3
    -----------
    Example 2:
        Input: nums = [2, 2, 1, 1, 1, 2, 2]
        Output: 2
    -----------
"""