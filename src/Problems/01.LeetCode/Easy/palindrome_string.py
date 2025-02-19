import re

# https://leetcode.com/problems/valid-palindrome/

# Removes all non-alphanumeric characters from the given string
# Regex [^a-zA-Z0-9]
def removeNonAlphanumeric(s):
    return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

# Recursively checks whether the given String is a Palindrome
# s = String, l = Left index, n = Size of Array
def recursion(s, l, n):
    if (l >= (n/2)):
        return True
    if (s[l] != s[n - l -1]):
        return False
    else:
        return recursion(s, l+1, n)
    
"""
    :type s: str
    :rtype: bool
"""
# Time Complexity: O(n/2) and Space Complexity: O(n/2)
def isPalindrome(s: str):
    s = removeNonAlphanumeric(s)
    l = 0
    n = len(s)

    return recursion(s, l, n)
    
print(isPalindrome("race a car"))

"""
    Example 1:
        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.
    -----------
    Example 2:
        Input: s = "race a car"
        Output: false
        Explanation: "raceacar" is not a palindrome.
    -----------
    Example 3:
        Input: s = " "
        Output: true
        Explanation: s is an empty string "" after removing non-alphanumeric characters.
        Since an empty string reads the same forward and backward, it is a palindrome.
"""