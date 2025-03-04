# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75


"""
    Time Complexity:  O(n + m)
    Space Complexity: O(n + m)
"""
def mergeAlternately(word1: str, word2: str) -> str:
    # Lengths of both strings
    length1, length2 = len(word1), len(word2)
    # Find the length of the shorter string
    min_length = min(length1, length2)

    # Using a list for better performance (O(1) append)
    # String concatenation inside loops (+=) is O(n²) due to immutable strings.
    # Using a list and ''.join() improves efficiency to O(n)
    merged_string = []
    
    # Merge characters alternately from both strings up to the shorter length
    i = 0
    while (i < min_length):
        merged_string.append(word1[i])
        merged_string.append(word2[i])
        i += 1
    
    # Append remaining characters from the longer string
    while (i < length1):
        merged_string.append(word1[i])
        i += 1
    while (i < length2):
        merged_string.append(word2[i])
        i += 1
    
    # Convert list to string efficiently
    return "".join(merged_string)


print(mergeAlternately("abc", "pqr"))    # apbqcr
print(mergeAlternately("ab", "pqrs"))    # apbqrs
print(mergeAlternately("abcd", "pq"))    # apbqcd



"""
    ----------
    Example 1: 
        Input: word1 = "abc", word2 = "pqr"
        Output: "apbqcr"
        Explanation: The merged string will be merged as so:
        word1:  a   b   c
        word2:    p   q   r
        merged: a p b q c r
    ----------
    Example 2: 
        Input: word1 = "ab", word2 = "pqrs"
        Output: "apbqrs"
        Explanation: Notice that as word2 is longer, "rs" is appended to the end.
        word1:  a   b 
        word2:    p   q   r   s
        merged: a p b q   r   s
    ----------
    Example 3:    
        Input: word1 = "abcd", word2 = "pq"
        Output: "apbqcd"
        Explanation: Notice that as word1 is longer, "cd" is appended to the end.
        word1:  a   b   c   d
        word2:    p   q 
        merged: a p b q c   d
    ----------
"""