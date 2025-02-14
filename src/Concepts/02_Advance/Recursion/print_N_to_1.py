# https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-n-to-1-without-loop

# Print Number N to 1
def print_N_to_1 (start):
    if (start < 1):    # Base Case
        return
    print(start, end = " ")
    print_N_to_1(start - 1)

print_N_to_1(10)    # 10 9 8 7 6 5 4 3 2 1
print()

# -----------------
# Using Backtracking (5 4 3 2 1), n = 5 -> Can't use (i-1)
print("Using Backtracking: ")
def backtracking(i, n):
    if (i > n):
        return
    backtracking(i + 1, n)
    print(i, end = " ")

backtracking(1, 5)
print()
