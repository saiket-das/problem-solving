# https://codeforces.com/problemset/problem/2065/A



# Test cases input
t: int = int(input())

while t > 0:
    # String input
    string: str = input()
    n = len(string)

    # Replace last 2 characters ('us') to `i` 
    if string[n - 1] == 's' and string[n - 2] == 'u':
        string = string[:n-2] + "i"
    print(string)

    t -= 1

