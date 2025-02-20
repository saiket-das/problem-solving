# https://leetcode.com/problems/longest-common-prefix/description/


"""
    :type strs: List[str]
    :rtype: str
"""
def longestCommonPrefix(strs):

    strs.sort()    # Time Complexity - O(nLog(n))
    prefix: str = ""

    # First and Last element
    first_element = strs[0]
    last_element = strs[-1]
    # Find MIN len from first and last element
    min_length = min(len(first_element), len(last_element))
    
    for i in range(min_length):
        if (first_element[i] != last_element[i]):
            return prefix
        else:
            prefix += first_element[i]

    return prefix

print(longestCommonPrefix(["aabbbcc", "aaaa", "aabb"]))

# Test cases
# ["abc", "aaa", "aab"]
# ["flower","flow","flight"]

"""
    ["aabbbcc", "aaaa", "aabb"]
    Steps:
    1. SORT the lsit (["aaa", "aab", "abc"])
    2. Take the FIRST and LAST index's value ("aaa" and "abc")
    3. Find the MIN LENGTH value between both value
    4. Check both value's prefex until it match ("aa") and save into a VARIABLE (prefix)
    5. Return the VARIABLE (prefix)
"""



