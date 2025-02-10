# O(n^2) Time Complexity

# Time Complexity - O(n^2)
def O_n_2 (n: int):
    for i in range(n):
        for j in range(n):
            print("*", end = " ")
        print()


def big_O_n_2 (n: int):
    for i, j in zip(range(n), range(n - 1, -1, -1)):
        for k in range(n):
            if (i == k or j == k):
                print("*", end = " ")
            else:
                print("·", end = " ")
        print()

O_n_2(10)
print("\n-------------------\n")
big_O_n_2(10)


# Time Complexity - O(n * m) -> (n = Length of Array 1 and m = Length of Array 2)
def O_n_m (arr1, arr2):
    for x in arr1:
        sum: int = 0
        for y in arr2:
            sum += (x * y)
        print("%d" %sum, end = " ")
        sum = 0
    print()

print("\n-------------------\n")
O_n_m([1, 2, 3, 4, 5], [10, 20])
