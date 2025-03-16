# https://leetcode.com/problems/most-common-word/description/


from collections import defaultdict
import re

"""
    Time Complexity: O(n) + O(n) + O(w) + O(m) + O(w)
    Space Complexity: O(n) + O(n)
"""
def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    # Replace commas with spaces to properly separate words
    paragraph = paragraph.replace(",", " ")

    # Remove punctuation and lowercase the text 
    cleaned_text = paragraph.translate(str.maketrans('', '', "!?';.")).lower()    # TC: O(n) + O(n) & SC: O(n) + O(n) 

    # Count word frequencies
    word_count = defaultdict(int)    # TC: O(w) & SC: O(w) -> `w` = The number of words
    for word in cleaned_text.split():
        word_count[word] += 1
    
    # Convert banned words to a set for quick lookup
    banned_words = set(banned)    # TC: O(m) & SC: O(m) -> `m` = The number of banned words

    most_frequent_word = ""
    max_frequency = 0

    print(word_count)
    # Identify the most common non-banned word
    for word, frequency in word_count.items():    # TC: O(w) + O(u) -> `u` = The number of unique words)
        if word in banned_words:
            continue  # Skip banned words

        if max_frequency < frequency:
            most_frequent_word = word
            max_frequency = frequency
    
    return most_frequent_word


# print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))    # "ball"
# print(mostCommonWord("a.", []))    # "a"
print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))    # "b"
    
"""
    Example 1:
        Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
        Output: "ball"
        Explanation: 
            "hit" occurs 3 times, but it is a banned word.
            "ball" occurs twice (& no other word does), so it is the most frequent non-banned word in the paragraph. 
            Note that words in the paragraph are not case sensitive,
            that punctuation is ignored (even if adjacent to words, such as "ball,"), 
            & that "hit" isn't the answer even though it occurs more because it is banned.
    
    Example 2:    
        Input: paragraph = "a.", banned = []
        Output: "a"
"""