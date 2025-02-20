# https://leetcode.com/problems/majority-element/description/


"""
    Time Complexity:  O(N) + O(N) -> O(N)
    Space Complexity: O(N)
"""
def majorityElement(nums: list[int]) -> int:
    # Dictionary to store element frequencies
    freq_dict = {}    # SC: O(N)

    # Count occurrences of each number
    for num in nums:    # TC: O(N)
        freq_dict[num] = freq_dict.setdefault(num, 0) + 1
    
    # Find the Element with the Maximum Frequency and Return
    return max(freq_dict, key=freq_dict.get)    # TC: O(N)

print(majorityElement([2, 2, 1, 1, 1, 2, 2]))


"""
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