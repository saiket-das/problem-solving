# https://leetcode.com/problems/valid-palindrome/description/

import re

"""
    Time Complexity:  O(n) + O(n) => O(n)
    Space Complexity: O(n) -> (The filtered string (`s`) requires extra space proportional to the input, **O(N)**)
"""

# Using Two Pointer
def isPalindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub("[^a-zA-Z0-9]", '' ,s).lower()    # TC: O(n) and SC: O(n)

    # Initialize two pointers (Left and Right)
    l, r = 0, len(s)-1

    # Compare characters symmetrically
    while (l <= r):    # TC: O(n)
        # Mismatch found, not a palindrome
        if (s[l] != s[r]):
            return False
        l += 1     # Move left pointer forward
        r -= 1     # Move right pointer backward
    
    # If all characters matched, it's a palindrome
    return True

print(isPalindrome(" "))

"""
    ------------
    Example 1:
        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.
    ------------
    Example 2:
        Input: s = "race a car"
        Output: false
        Explanation: "raceacar" is not a palindrome.
    ------------
    Example 3:
        Input: s = " "
        Output: true
        Explanation: `s` is an empty string "" after removing non-alphanumeric characters.
                     Since an empty string reads the same forward and backward, it is a palindrome.
    ------------
"""