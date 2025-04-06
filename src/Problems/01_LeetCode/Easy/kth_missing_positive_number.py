# https://leetcode.com/problems/kth-missing-positive-number/description/



"""
    Brute Force: Linear Search
        Time Complexity:  O(1000)
        Space Complexity: O(1)
"""
def brute_froce(arr: list[int], k: int) -> int:
    # Get the length of the list
    n = len(arr)
    
    """
        Initialize pointers:
        `missing_count` tracks how many missing numbers we've seen so far
        `arr_pointer` tracks the current index in the sorted array
        `upper_bound` is the max number we'll iterate to (covers constraints)
    """
    missing_count, arr_pointer, upper_bound = 0, 0, 1001

    for num in range(1, upper_bound):
        # If current number is in the array, skip it (not missing)
        if arr_pointer < n and num == arr[arr_pointer]:
            arr_pointer += 1
        else:
            # Otherwise, it's a missing number
            missing_count += 1
        
        # If we've found the k-th missing number, return it
        if missing_count == k:
            return num



"""
    Better: Linear Search
        Time Complexity:  O(n) -> O(1000)
        Space Complexity: O(1)
"""
def better(arr: list[int], k: int) -> int:
    # Get the length of list
    n = len(arr)

    for i in range(n):
        # If the current element is less than or equal to k, it's not missing — shift k forward
        if arr[i] <= k:
            k += 1  # Shif k
        else:
            break
    
    # Return the k-th missing number
    return k



"""
    Optimal: Binary Search
        Time Complexity:  O(log n)
        Space Complexity: O(1)
"""
def optimal(arr: list[int], k: int) -> int:
    # Get the length of the list
    n = len(arr)

    # Two pointer
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        # Number of missing elements until arr[mid]
        missing = arr[mid] - (mid + 1)

        if missing < k:
            low = mid + 1     # Move right if we haven't found k missing numbers yet
        else:
            high = mid - 1    # Potential position, move left
    
    # Final answer using formula
    return low + k
            


# Main function
def findKthPositive(arr: list[int], k: int) -> int:
    # print(brute_froce(arr, k))
    # print(better(arr, k))
    print(optimal(arr, k))


findKthPositive([1,2,3,4], 2)       # 6 [5,(6)]
findKthPositive([2,3,4,7,11], 5)    # 9 [1,5,6,8,(9)]
findKthPositive([1],999)            # 1000
findKthPositive([4,7,9], 3)         # 3



"""
    Example
      [2,3,4,7,11], k = 5
      - index: 0 -> element (2)  < k (5)
      - index: 1 -> element (3)  < k (6)
      - index: 2 -> element (4)  < k (7)
      - index: 3 -> element (7)  < k (9)
      - index: 3 -> element (11) > k (9) Break;
    
    Return = k (6)
"""


"""
    --------------------------------------------
    Example: Optimal Solution
    --------------------------------------------
    Input     arr = [2, 3, 4, 7, 11]     
    k = 5   
    
    Index    ->  0   1   2   3    4
    Array    ->  2   3   4   7   11
    Missing  ->  1   1   1   3    6
                            ↑H   ↑L   (After binary search)
    --------------------------------------------
    Formula:

     ans = arr[high] + (k - missing)
         = arr[high] + k - (arr[high] - (high + 1))
         = high + 1 + k
         = low + k   ← (since low = high + 1 after loop)
    --------------------------------------------
"""
