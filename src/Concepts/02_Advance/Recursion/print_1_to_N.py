# https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1

# Print number 1 to N
def print_1_to_N (start, end):
    if (start == end):
        return
    print(start + 1, end = " ")
    print_1_to_N(start + 1, end)

print_1_to_N(0, 10)
print()


# -----------------
# Using Backtracking
print("Using Backtracking")
def one_to_n (i):
    if (i < 1):    # Base Case
        return
    one_to_n(i-1)
    print(i, end = " ")

one_to_n(10)
print()
