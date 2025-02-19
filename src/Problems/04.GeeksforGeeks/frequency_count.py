# https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0


def frequencyCount(arr):
    # Get the Length of Array
    N = len(arr)
    # Initialize with 0 for 1 to N (Length of Array)
    freq_dict = {i: 0 for i in range(1, N+1)}

    for x in arr:
        # Increment count
        freq_dict[x] += 1
    
    # Return only Values as List
    return list(freq_dict.values())

result = frequencyCount([2, 3, 2, 3, 5])   
print(result)


"""
    Example 1:
        Input: arr[] = [2, 3, 2, 3, 5]
        Output: [0, 2, 2, 0, 1]
        Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.
    -----------
    Example 2:
        Input: arr[] = [3, 3, 3, 3]
        Output: [0, 0, 4, 0]
        Explanation: We have: 1 occurring 0 times, 2 occurring 0 times, 3 occurring 4 times, and 4 occurring 0 times.
    -----------
    Example 3:
        Input: arr[] = [1]
        Output: [1]
        Explanation: We have: 1 occurring 1 time, and there are no other numbers between 1 and the size of the array.
    -----------
    Example 3:
        Input: arr[] = [2, 1]
        Output: [2, 1, 0]
        Explanation: We have: 1 occurring 1 time, and there are no other numbers between 1 and the size of the array.
"""