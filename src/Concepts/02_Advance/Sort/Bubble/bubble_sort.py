# Bubble Sort

# Time Complexity: O(n^2) and Space Complexity: O(1)
def bubble_sort(arr: list[int]) -> list[int]:
    # Get the length of the array
    N: int = len(arr)

    # Perform N-1 passes through the array
    for i in range(N-1):
        # Track if any Swaps were made in this pass
        swapped = False

        # Compare Adjacent Elements and Swap if needed
        for j in range(N-i-1):    # Ignore the Last 'i' sorted elements
            if (arr[j+1] < arr[j]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True    # Mark Swap as done
        
        # If NO Swaps occurred, the array is already Sorted
        if (swapped == False):
            break

    return arr

result = bubble_sort([1, 2, 3, 5, 3, 1])
print(result)

"""
    [50, 40, 60, 30, 45, 10]
    [1, 3, 5, 3, 2, 1]
"""