# https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=leaders-in-an-array


"""
    Brute Force: Nester Loop
        Time Complexity:  O(n^2)
        Space Complexity: O(n)
"""
def brute_force(arr):
    # Get the length of the array
    n = len(arr)
    # Initialize a list to store leader elements
    result = []

    # Iterate through each element in the array
    for i in range(n):
        # Assume the current element is a leader
        is_leader = True

        # Compare with all elements to its right
        for j in range(i, n):
            # If a larger element is found, it's not a leader
            if arr[i] < arr[j]:
                is_leader = False
                break    # No need to check further, exit the loop
        
        # If the element remains a leader, add it to the result list
        if is_leader:
            result.append(arr[i])    # Add it to the leaders list
    
     # Return the list of leaders
    return result


"""
    Optimal: Linear Loop
        Time Complexity:  O(n) + O(n) => O(2n)
        Space Complexity: O(n)
"""
def optimal(arr):
    # Get the length of the array
    n = len(arr)
    # Initialize a list to store leader elements
    result = []

    # Track the maximum element encountered from the right
    max_from_right = -1

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # If the current element is greater than or equal to max_from_right
        if max_from_right <= arr[i]:
            result.append(arr[i])      # Add it to the leaders list
            max_from_right = arr[i]    # Update max_from_right to the current element
    
    # Reverse the list to maintain the original order
    result.reverse()
    return result


# Main Function
def leaders(arr):
    print(brute_force(arr))
    print(optimal(arr))


leaders([16, 17, 4, 3, 5, 2])
leaders([10, 4, 2, 4, 1])
leaders([5, 10, 20, 40])
leaders([30, 10, 10, 5])


""" 
    ** When an array is sorted in non-increasing order, all elements are leaders. **

    ----------
    Example 1:
        Input: arr = [16, 17, 4, 3, 5, 2]
        Output: [17, 5, 2]
        Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
    ----------
    Example 2:
        Input: arr = [10, 4, 2, 4, 1]
        Output: [10, 4, 4, 1]
        Explanation: Note that both of the 4s are in output, 
                     as to be a leader an equal element is also allowed on the right side
    ----------
    Example 3:
        Input: arr = [5, 10, 20, 40]
        Output: [40]
        Explanation: When an array is sorted in increasing order, only the rightmost element is leader.
    ----------
    Example 4:
        Input: arr = [30, 10, 10, 5]
        Output: [30, 10, 10, 5]
        Explanation: When an array is sorted in non-increasing order, all elements are leaders.
    ----------
"""
