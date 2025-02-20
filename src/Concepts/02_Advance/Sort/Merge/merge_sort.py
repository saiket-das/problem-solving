# Merge Sort


# ------ Divide ------
"""
    Time Complexity: O(logN)  -> (Because the array is divided into halves)
    Space Complexity: O(logN) -> (Recursive call stack depth for divide function)
"""
def divide (arr: list[int], low: int, high: int):
    # Base case: Stop recursion when only one element is left
    if (low >= high):
        return
    
    # Find the middle index to divide the array
    mid = (high + low) // 2
    # Recursively divide the left and right halves
    divide(arr, low, mid)       
    divide(arr, mid + 1, high)

    # Merge the sorted halves
    merge(arr, low, mid, high)


# ------ Merge ------
"""
    Time Complexity: O(N)  -> (Each element is visited once and placed in temp array)
    Space Complexity: O(N) -> (Temporary list 'temp' to store sorted elements) 
"""
def merge (arr: list[int], low: int, mid: int, high: int):
    # Temporary list to store merged elements
    temp: list[int] = []

    # Pointers for left and right halves
    left, right = low, mid + 1

    # Merge elements from both halves in sorted order
    while ((left <= mid) and (right <= high)):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    # Append remaining elements from the Left half (if any)
    while (left <= mid):
        temp.append(arr[left])
        left += 1
    # Append remaining elements from the Right half (if any)
    while (right <= high):
        temp.append(arr[right])
        right += 1
    
    # Copy sorted elements back to the original array
    for i in range(low, high + 1):
        arr[i] = temp[i-low]


# ------ Merge Sort ------
"""
    Time Complexity: O(NlogN)
        Divide: O(logN) * Merge: O(N) = O(NlogN)
    Space Complexity: O(N) 
        Divide: O(logN) + Merge: O(N) = O(N)
"""
def merge_sort(arr: list[int]) -> list[int]:
    # Find Low and High
    low, high = 0, len(arr) - 1
    # Call 'divide' function
    divide(arr, low, high)
    # Return Original Array
    return arr


result = merge_sort([50, 40, 60, 30, 45, 10])
print(result)

"""
    [50, 40, 60, 30, 45, 10]
    [1, 3, 5, 3, 2, 1]
    [5, 2, 3, 2, 1]
"""