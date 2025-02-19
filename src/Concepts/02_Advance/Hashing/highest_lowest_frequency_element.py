# https://takeuforward.org/arrays/find-the-highest-lowest-frequency-element/

# TC -> Time Complexity and SC -> Space Complexity
# TC: O(n) + O(n) = O(n) and SC: O(n)
def highest_lowest_freq_elements(arr: list[int]) -> list[int]:
    # Initialize Dictionary -> SC: O(n)
    freq_dict = {}

    for x in arr:    # TC: O(n)
        # Increment value
        freq_dict[x] = freq_dict.setdefault(x, 0) + 1
    
    # Find Max and Min frequency element -> TC: O(n) + O(n) = O(n)
    min_elem = min(freq_dict, key=freq_dict.get)
    max_elem = max(freq_dict, key=freq_dict.get)

    # Return as List
    return [max_elem, min_elem]

result = highest_lowest_freq_elements([2, 2, 3, 4, 4, 2])
print(result)

"""
    -----------
    Example 1:
        Input: array[] = {10,5,10,15,10,5};
        Output: 10 15
        Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.
    -----------    
    Example 2:
        Input: array[] = {2,2,3,4,4,2};
        Output: 2 3
        Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.
    -----------
"""


