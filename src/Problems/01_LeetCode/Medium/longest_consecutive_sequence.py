# https://leetcode.com/problems/longest-consecutive-sequence/description/

"""
    Brute Force: Nested Loop
        Time Complexity:  O(n^2)
        Space Complexity: O(1)
"""
def linear_search(nums: list[int], target: int) -> bool:
    for num in nums:
        if num == target:
            return True
    return False

def brute_force(nums: list[int]) -> int:
    # Variable to store the longest consecutive sequence length
    longest_streak = 1

    # Iterate through each number and check for consecutive numbers
    for num in nums:
        # Start from the current number
        current_num = num
        # Initialize the streak length to 1
        current_streak = 1

        # Continue searching for consecutive numbers
        while linear_search(nums, current_num + 1):
            # Move to the next consecutive number
            current_num += 1
            # Increase the streak length
            current_streak += 1
        
        # Update the longest streak found so far
        longest_streak = max(current_streak, longest_streak)

    return longest_streak


"""
    Better: Sorting
        Time Complexity:  O(n log n) + O(n)
        Space Complexity: O(1)
"""
def better(nums: list[int]) -> int:
    # Sort the array to bring consecutive numbers together
    nums.sort()

    # Variable to store the longest consecutive sequence length
    longest_streak = 1              # Stores the maximum consecutive sequence length
    current_streak = 0              # Tracks the current sequence length
    previous_num = float('-inf')    # Keeps track of the last valid consecutive number

    # Iterate through the sorted array to count consecutive sequences
    for num in nums:
        # If current number extends the sequence
        if num == previous_num + 1:
            current_streak += 1
        # Reset streak if duplicate or non-consecutive number
        elif num != previous_num:
            current_streak = 1
        
        # Update the previous number tracker
        previous_num = num
        # Update max streak
        longest_streak = max(current_streak, longest_streak)

    return longest_streak


""" 
    Optimal:
        Time Complexity:  O(n) + O(n + n) => O(3n)
        Space Complexity: O(n)
    ---------------------
    Thought Process:
    Approach: Set
        1. Convert the array into a HashSet
            - This allows quick lookups (O(1) average time complexity).
            - Avoids duplicates (since sets automatically remove them).
        
        2. Initialize a variable longest_streak
            - Tracks the length of the longest consecutive sequence found.
        
        3. Iterate through each number in the set
            - Identify sequence start points:
                - A number is the start of a new sequence if (num - 1) is NOT in the set.
                - If (num - 1) exists, it means num is part of a sequence that has already been counted.
        4. Expand the sequence from the start point 
            - If num is a start point:
            - Set current_streak = 1 (since it includes itself).
            - Check if num + 1, num + 2, … exist in the set.
            - Continue until a number is missing.
            - Update longest_streak if current_streak is greater.
        5. Skip non-starting numbers
            - If (num - 1) exists in the set, skip num, as it belongs to an already processed sequence.
            
    ** This approach ensures an efficient O(n) runtime by avoiding redundant checks. **
"""
def optimal(nums: list[int]) -> int:
    # Convert the array into a Set for O(1) lookups
    num_set: set = set(nums)
    # Track the longest consecutive sequence
    longest: int = 0

    for num in num_set:
        # Check if this number is the start of a sequence
        if (num - 1) not in num_set:
            current_streak = 1
            # Expand the sequence by checking for consecutive numbers
            while (num + current_streak) in num_set:
                current_streak += 1

            # Update the longest sequence found so far
            # Find longest consecutive from current and previous streak
            longest = max(current_streak, longest)

    return longest


def longestConsecutive(nums: list[int]) -> int:
    # print(brute_force(nums))
    print(better(nums))

longestConsecutive([0,3,7,2,5,8,4,6,0,1])    # 9
longestConsecutive([100,4,200,1,3,2])        # 4
longestConsecutive([1,0,1,2])                # 3


"""
    --------------
    Constraints:
        0 <= nums.length <= 105
        -109 <= nums[i] <= 109
    -------------
    Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    --------------
    Example 2:    
        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9
    --------------
    Example 3:    
        Input: nums = [1,0,1,2]
        Output: 3
    --------------
"""