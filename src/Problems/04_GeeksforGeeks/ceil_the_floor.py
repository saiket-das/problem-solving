# https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=ceil-the-floor



"""
    Approach: Binary Search (Upper bound)
"""
def upper_bound(x: int, arr: list) -> list:
    # Get the length of the array
    n = len(arr)

    # Initialize search boundaries
    low, high = 0, n - 1

    ans = n
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # maybe an answer
        if arr[mid] > x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    
    return ans



def answer(x: int, arr: list) -> list:
    arr.sort()
    n = len(arr)

    low, high = 0, n - 1

    floor, cell = -1, -1
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            floor = arr[mid]
            low =  mid + 1
        elif arr[mid] > x:
            cell = arr[mid]
            high = mid - 1
        else:
            floor = cell = arr[mid] 
            return [floor, cell]
    
    return [floor, cell]
                    




# Main Function
def getFloorAndCeil(x: int, arr: list) -> list:
    # print(upper_bound(x, arr))
    print(answer(x, arr))


# Main function
getFloorAndCeil(7, [5, 6, 8, 9, 6, 5, 5, 6])     # 6, 8
getFloorAndCeil(7, [7, 7, 7, 8, 9, 9, 10, 10])     # 6, 8
getFloorAndCeil(10, [5, 6, 8, 8, 6, 5, 5, 6])    # 8, -1