# https://codeforces.com/problemset/problem/2062/A


def string():
    # Test case input
    t: int = int(input())

    while (t > 0):
        # Word input (e.g., "10101")
        word: str = input()

        # Initialize sum to store the total numeric value of characters
        sum: int = 0
        for ch in word:
            # Convert character to integer and add to sum
            sum += ord(ch) - ord('0')
        
        # Print answer (sum)
        print(sum)
        t -= 1

string()


"""
Input:
5
1
000
1001
10101
01100101011101

Output
1
0
2
3
8

"""