# Selection Sort

# Time Complexity: O(n^2) and Space Complexity: O(1)
def selection_sort (arr: list[int]) -> list[int]:
    # Get the length of the array
    N: int = len(arr)    

    # Iterate until (0 to N-1)
    # Time Complexity: O(n)
    for i in range(N-1):
        # Assume the current element is the smallest
        min_index: int = i

        # Iterate through the unsorted portion of the array (i+1 to N-1)
        # Time Complexity: O(n)
        for j in range(i + 1, N):
            # If a smaller element is found, update min_ele and its index
            if (arr[j] < arr[min_index]):
                min_index = j
        
        # Swap the Smallest element found with the element at Index i
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr


result = selection_sort([1, 3, 5, 3, 2, 1])
print(result)

"""
    [50, 40, 60, 30, 45, 10]
    [1, 3, 5, 3, 2, 1]
"""