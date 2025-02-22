# https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict

"""
    Time Complexity:  O(m * n)
    Space Complexity: O(m * n)
"""
def groupAnagrams(strs: list[str]) -> list[list[str]]: 
    """
        The dictionary stores anagram groups using a character frequency tuple as the key.
        Since lists are mutable and cannot be dictionary keys, we use a tuple instead (immutable).
        Example: { (1, 0, 0, 0, 1, 0, ..., 1, 0): ["ate", "eat", "tea"] }
    """
    # Dictionary to store anagrams grouped by character count as a tuple
    anagram_groups = defaultdict(list)

    # TC: O(m) -> (m = Number of Strings)
    for st in strs:      
        # Character frequency array for 26 (a...z) lowercase English letters
        char_count = [0] * 26

        # Populate character count for the current word
        # TC: O(n) -> (n = String Length)
        for char in st:    
            char_count[ord(char) - ord('a')] += 1
        
        # Convert the list to a tuple (hashable) and use it as a key
        anagram_groups[tuple(char_count)].append(st)
    
    # Return values of anagrams as a list
    return list(anagram_groups.values())

result = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)

"""
    ["eat","tea","tan","ate","nat","bat"]
    [""]
    ["a"]
"""

"""
    -----------
    Example 1:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        Explanation:
            There is no string in strs that can be rearranged to form "bat".
            The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
            The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
    -----------
    Example 2:
        Input: strs = [""]
        Output: [[""]]
    -----------
    Example 3:
        Input: strs = ["a"]
        Output: [["a"]]
    -----------
"""