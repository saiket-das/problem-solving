# Quick Sort Descending Order


def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while (i < j):
        while (pivot <= arr[i] and i <= high - 1):
            i += 1
        while (arr[j] < pivot and low + 1 <= j):
            j -= 1
        
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
        
    
    arr[low], arr[j] = arr[j], arr[low]

    return j

def quick_sort_descending(arr, low, high):
    if (low < high):
        p_index = partition(arr, low, high)
        quick_sort_descending(arr, low, p_index - 1)
        quick_sort_descending(arr, p_index + 1, high)
    
    return arr

# Main function
if __name__ == "__main__":
    arr = [4, 6, 2, 4, 5, 7, 9, 1, 3]
    low = 0
    high = len(arr) - 1
    
    result = quick_sort_descending(arr, low, high)
    print(result)