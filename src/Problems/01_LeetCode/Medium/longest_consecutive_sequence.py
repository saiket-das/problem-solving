# https://leetcode.com/problems/longest-consecutive-sequence/description/


from collections import defaultdict


""" 
    Time Complexity:  O(N)
    Space Complexity: O(N)
    ---------------------

    Thought Process:
        Approach 1: Sorting
          - Sorting the array requires O(N log N) time, which is not optimal. ❌
        
        Approach 2: Set
            - Convert the array into a set to allow O(1) lookups.
            - Initialize a variable `longest` to track the longest consecutive sequence.
            - Iterate through each element in the set:
                1. Identify potential sequence start points: 
                    - A number is the start of a sequence if (num - 1) is not in the set.
                2. If a number is a start point:
                    - Initialize `streak = 1` to track sequence length.
                    - Keep checking for the next consecutive numbers (num + 1, num + 2, ...).
                    - Stop when the next number is missing.
                    - Update `longest` to store the maximum sequence length encountered.
                3. If a number is not a start point (num - 1 exists), skip it, as it belongs to an already counted sequence.
            
            ** This approach ensures an efficient O(N) runtime by avoiding redundant checks. **
"""

def longestConsecutive(nums: list[int]) -> int:
    # Convert the array into a set for O(1) lookups
    num_set: set = set()
    for num in nums:
        num_set.add(num)
    
    # Track the longest consecutive sequence
    longest  = 0

    for num in num_set:
        # Check if this number is the start of a sequence
        if (num - 1) not in num_set:
            streak = 1
            # Expand the sequence by checking for consecutive numbers
            while (num + streak) in num_set:
                streak += 1

            # Update the longest sequence found so far
            # Find longest consecutive from current and previous streak
            longest = max(streak, longest)

    return longest

print(longestConsecutive([1,0,1,2]))


"""
    --------------
    Target TC: O(n)
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