# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1?track=DSASP-Searching&amp%253BbatchId=154&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=floor-in-a-sorted-array



"""
    Approach: Binary Search (Lower bound)
        Time Complexity: O(log n)
        Space Complexity: O(log n)
"""
def lower_bound(arr, x):
    # Get the length of the array
    n = len(arr)

    # Initialize search boundaries
    low, high = 0, n - 1

    ans = n
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    
    return ans



def answer(arr, x):
    # Get the length of the array
    n = len(arr)

    # Initialize search boundaries
    low, high = 0, n - 1

    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # Element found, return its index
        if arr[mid] == x:
            # Move forward to find the last occurrence of the target element
            while True:
                # Ensure we don't go out of bounds and check if the next element is the same
                if mid < n - 1 and arr[mid] == arr[mid + 1]:
                    mid += 1      # Move to the next occurrence
                else:
                    return mid    # Return the index of the last occurrence
            
        elif arr[mid] < x:
            low = mid + 1     # Search in the right half
        else:
            high = mid - 1    # Search in the left half
    
    return low - 1 if low != -1 else -1



 # Binary Search


# Main Function
def findFloor(arr, x):
    # print(lower_bound(arr, x))
    print(answer(arr, x))


findFloor([1, 2, 8, 10, 10, 12, 19], 11)        # 3
findFloor([1, 2, 8, 10, 10, 12, 19], 5)         # 1
findFloor([1, 2, 8, 10, 10, 12, 19], 0)         # 0
findFloor([0, 2, 8, 10, 10, 12, 19], 1)         # 0
findFloor([1, 2, 8, 10, 10, 10, 12, 19], 11)    # 6
findFloor([1, 1, 1, 1, 1, 1, 1, 1], 10)
findFloor([4, 15, 17, 17, 19, 20, 21, 22, 
           22, 25, 26, 26, 26, 28, 28, 28, 
           31, 31, 32, 33, 34, 34, 35, 36, 
           36, 37, 38, 38, 39, 41, 41, 42, 
           43, 43, 44, 44, 45, 45, 46, 47, 
           49, 49, 50, 50, 50, 51, 53, 54, 
           54, 56, 57, 58, 58, 59, 60, 64, 
           67, 69, 75, 94], 26)    # 12


