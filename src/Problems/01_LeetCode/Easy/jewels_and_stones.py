# https://leetcode.com/problems/jewels-and-stones/description/


from collections import defaultdict

"""
    Approach: HashMap
        Time Complexity:  O(n + m)
        Space Complexity: O(n)

        `n` = The length of 'stones' str and `m` = The length of 'jewels' str
"""
def optimal(jewels: str, stones: str) -> int:
    # Create a dictionary to store the frequency of each stone
    freq_map = defaultdict(int)

    # Count the occurrences of each stone in the 'stones' string
    for stone in stones:
        freq_map[stone] += 1
    
    # Initialize a counter to track the number of jewels found in stones
    result = 0

    # Iterate through each character in 'jewels' and sum up its count from freq_map
    for ch in jewels:
        result += freq_map[ch]

    return result


# Main Function
def numJewelsInStones(jewels: str, stones: str) -> int:
    print(optimal(jewels, stones))


numJewelsInStones("z", "ZZ")          # 3
numJewelsInStones("aA", "aAAbbbb")    # 3
