from collections import defaultdict
from collections import Counter


# https://leetcode.com/problems/valid-anagram/description/

# Time Complexity: O(N) + O(N) + O(N) -> O(N) and Space Complexity: O(N) 
def isAnagram(s: str, t: str) -> bool:
    # Solution 1: Sorting
    """
    s = sorted(s)
    t = sorted(t)

    return True if (s == t) else False
    """
    # Solution 2: Hash Table
    freq_map = defaultdict(int)    # SC: O(N)

    # Count occurrences of each character in `s` string
    for ch in s:    # TC: O(N)
        freq_map[ch] += 1
    
    # Subtract occurrences for each character in `t` string
    for ch in t:    # TC: O(N)
        freq_map[ch] -= 1
    
    # If any frequency is nonzero, `s` and `t` are not anagrams (return false)
    for value in freq_map.values():    # TC: O(N)
        if (value != 0):
            return False
    
    return True

"""
    Time Complexity:  O(N)
    Space Complexity: O(1) -> O(26) (s and t consist of lowercase English letters)
"""
def isAnagram(s: str, t: str) -> bool:
    # Use Counter to create frequency maps for both strings
    s_counter = Counter(s)
    t_counter = Counter(t)

    # Compare the two frequency maps
    return s_counter == t_counter


print(isAnagram("anagram", "nagaram"))

# "anagram", "nagaram"
# "rat", "car"

"""
    Solution 1 (Sorting Approach):
        Steps: 
            - Sort both strings and compare them.
            - If they are equal, they are anagrams.
        Time Complexity: O(N log N) + O(N log N) = O(N log N) (due to sorting)
        Space Complexity: O(1) (if sorting is done in-place)
    ----------------
    Solution 2 (Frequency Count Approach):
        Steps:
            - Initialize a frequency dictionary (freq_map).
            - Count the frequency of characters in the first ('s') string.
            - Subtract the frequency of characters from the second ('t') string.
            - If any frequency remains non-zero, return False.
        Time Complexity: O(N) + O(N) + O(N) = O(N)
        Space Complexity: O(N) (for storing frequency counts)
    ----------------
    Solution 2 (Frequency Count Approach (Shortcut)):
        Steps:
            - Count frequency of Both String using Counter function (from collections import Counter) 
            - Return their compare value
        Time Complexity: O(N) + O(N) + O(N) = O(N)
        Space Complexity: O(N) (for storing frequency counts)


"""
