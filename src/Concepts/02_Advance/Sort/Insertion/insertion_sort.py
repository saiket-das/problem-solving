# Insertion Sort

# Time Complexity: O(n^2) and Space Complexity: O(1)
def insertion_sort(arr: list[int]) -> list[int]:
    # Iterate through the array, considering one element at a time
    for i in range(len(arr)):
        j = i    # Start with the current element

        # Shift elements in the sorted part of the array to the Right
        # Until we find the correct position for arr[j]
        while ((j > 0) and (arr[j] < arr[j-1])):
            # Swap the current element with the previous one
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1    # Move one position back to continue checking

    return arr

result = insertion_sort([50, 40, 60, 30, 45, 10])
print(result)

"""
    [50, 40, 60, 30, 45, 10]
    [1, 3, 5, 3, 2, 1]
"""