# https://www.geeksforgeeks.org/problems/second-largest3735/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=second-largest


"""
    Approach 1:
        Time Complexity:  O(n) + O(n) => O(n)
        Space Complexity: O(1)
    
    Approach 2:
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""


def getSecondLargest(arr):

    """
    # Approach 1
        # Find the largest number in the list
        largest = -1
        for num in arr:
            largest = max(num, largest)
        
        # Find the second largest number
        second_largest = -1
        for num in arr:
            # Only consider numbers smaller than the largest
            if (num < largest):
                second_largest = max(num, second_largest)

        return -1 if (second_largest == largest)  else second_largest
    """
    
    # Approach 2
    
    # Not enough elements to determine a second largest number
    if (len(arr) < 2):
        return - 1
    
    # Initialize largest with the first element
    largest = arr[0]
    # Default to -1, assuming no second largest exists initially
    second_largest = -1

    for num in arr:
        # If current number is greater than the largest, update both largest and second largest
        if (largest < num):
            second_largest = largest    # Previous largest becomes second largest
            largest = num               # Update largest with the new maximum

        # If current number is smaller than largest but greater than second largest, update second largest
        elif (num < largest and second_largest < num):
            second_largest =  num
    
    # Returns -1 if no valid second largest number was found
    return second_largest

print(getSecondLargest([28078, 19451, 935, 28892, 2242, 3570, 5480, 231]))
print(getSecondLargest([12, 35, 10, 2, 34, 11]))
print(getSecondLargest([10, 5, 10]))
print(getSecondLargest([7, 7, 7, 7]))

"""
    Test cases:
        [7, 7, 7, 7]
        [10, 5, 10]
        [12, 35, 10, 2, 34, 11]
        28078, 19451, 935, 28892, 2242, 3570, 5480, 231]
"""

"""
    ** Without Sorting **
    Steps:
      - Find Largest element first
      - Find Second largest element based on Largest number 
"""