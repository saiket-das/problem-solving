# Quick Sort

"""
    Time Complexity: O(n log n)
    Space Complexity: O(1)
"""

def partition(arr, low, high):
    """
      - Partitions the array around a pivot element.
      - The pivot is chosen as the first element. The function rearranges the array
        so that elements smaller than the pivot are on the left and larger elements 
        are on the right.
      - Returns the final position of the pivot.
    """
     # Choosing the first element as the pivot
    pivot = arr[low]
    i = low
    j = high

    while (i < j):
        # Move i forward until finding an element greater than the pivot
        while (arr[i] <= pivot and i <= high - 1):
            i += 1
        
        # Move j backward until finding an element smaller than or equal to the pivot
        while (arr[j] > pivot and low + 1 <= j):
            j -= 1
        
        # Swap misplaced elements
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot in its correct sorted position
    arr[low], arr[j] = arr[j], arr[low]
    
    # Return the partition index
    return j


def quick_sort(arr, low, high):
    """
        Recursively applies QuickSort by partitioning the array and sorting subarrays.
    """
    if (low < high):
        p_index = partition(arr, low, high)     # Get partition index
        quick_sort(arr, low, p_index - 1)       # Sort the left subarray
        quick_sort(arr, p_index + 1, high)      # Sort the right subarray
    
    # Return the sorted array
    return arr

# Main function
if __name__ == "__main__":
    arr = [4, 6, 2, 4, 5, 7, 9, 1, 3]
    low = 0
    high = len(arr) - 1
    
    result = quick_sort(arr, low, high)
    print(result)


"""
    Pseudocode:

        quick_sort(arr, low, high)
            if (low < high)
                partition = divide(arr, low, high)
                quick_sort(arr, low, partition-1)
                quick_sort(arr, partition+1, high)
        
        divide(arr, low, high)
            pivot = arr[low]
            i = low
            j = high
            
            while (i < j)
                while (arr[i] < pivot and i <= high-1)
                        i++
                while (arr[i] > pivot and low <= j-1 )
                        j--
                if (i < j)
                    swap(arr[i], arr[j])
            
            swap(arr[low], arr[j])
            return j    # Partition index                   
"""

""" 
    [4, 6, 2, 5, 7, 9, 1, 3]
    Steps:
      - Pick any pivot (Means any element) and Place it in its correct place (let's pick `4`)
      - Smaller on the left and Larger on the right
      - Recursively Sort
        ------------------------
        [4, 6, 2, 5, 7, 9, 1, 3]
                  4
        ------------------------
        [2, 1, 3, 4, 6, 5, 7, 9]
        --------     -----------
         Smaller       Larger
        ------------------------
        [2, 1, 3]    [6, 5, 7, 9]
            2            6
        --------     ------------
        [1, 2, 3]    [5, 6, 7, 9]   
"""