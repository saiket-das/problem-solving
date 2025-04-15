

"""
    TC: O(n) + O(k) + O(n)
    SC: O(n)
    
    `k` = Number of words
"""
def bruteForce(s: str) -> str:    
    return ' '.join(s.split()[::-1])


def reverseWords(s: str) -> str:
    print(bruteForce(s))

reverseWords("the sky is blue")     # "blue is sky the"
reverseWords("  hello world  ")     # "world hello"
reverseWords("a good   example")    # "example good a"