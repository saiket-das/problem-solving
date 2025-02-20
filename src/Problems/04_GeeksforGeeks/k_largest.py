# https://www.geeksforgeeks.org/problems/k-largest-elements4206/1

"""
    Time Complexity: O(n log n) + O(k) -> O(n log n)
    Space Complexity: O(k) (for storing results)
"""
def kLargest(arr: list[int], k: int) -> list[int]:
    # Sort the array in Descending order
    arr.sort(reverse = True)    # TC: O(n log n)

    # Extract the first 'k' largest elements
    result: list[int] = []    # SC: O(k)
    for i in range(k):    # TC: O(k)
        result.append(arr[i])    

    return result

print(kLargest([12, 5, 787, 1, 23], 2))

"""
    -----------
    Example 1:
        Input: arr[] = [12, 5, 787, 1, 23], k = 2
        Output: [787, 23]
        Explanation: 1st largest element in the array is 787 and second largest is 23.
    -----------
    Example 2:
        Input: arr[] = [1, 23, 12, 9, 30, 2, 50], k = 3 
        Output: [50, 30, 23]
        Explanation: Three Largest elements in the array are 50, 30 and 23.
    -----------
    Example 3:
        Input: arr[] = [12, 23], k = 1
        Output: [23]
        Explanation: 1st Largest element in the array is 23.
    -----------
"""