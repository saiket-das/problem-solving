# https://codeforces.com/problemset/problem/71/A


def way_too_long_words():
    # Test cases
    t: int = int(input())

    while (t > 0):
        word: str = str(input())
        N = len(word)
        # If the Length is less than 10
        if ( N < 10):
            print(word)
        # If the Length of Word is more than 10
        else:
            # First element + Length of Substring (0 to N-1) + Last element
            print("%s%s%s" %(word[0], len(word[1:N-1]), word[N-1]))
            
        t -= 1

way_too_long_words()



"""
--------------
Input:
5
abcdefgh
abcdefghi
abcdefghij
abcdefghijk
abcdefghijklm
--------------
Output: 
abcdefgh
abcdefghi
abcdefghij
a9k
a11m
"""