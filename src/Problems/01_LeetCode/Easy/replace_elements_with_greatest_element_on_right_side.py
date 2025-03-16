# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

"""
    Time Complexity:  O(n)
    Space Complexity: O(1)
"""
def replaceElements(arr: list[int]) -> list[int]:
    # Get the length of the array
    n = len(arr)
    # Variable to store the maximum element seen from the right
    max_right = -1

    # Traverse the array from right to left (excluding the last element)
    for i in range(n - 1, -1, -1):
        # Compute the new max before overwriting
        new_max = max(max_right, arr[i])
        # Replace the current element with max_right
        arr[i] = max_right
        # Update max_right for the next iteration
        max_right = new_max 

    return arr

print(replaceElements([17,18,5,4,6,1]))    # [18,6,6,6,1,-1]
print(replaceElements([19,18,5,4,6,1]))    # [18,6,6,6,1,-1]
print(replaceElements([400]))              # [-1]


"""
    ---------
    Example 1:
        Input: arr = [17,18,5,4,6,1]
        Output: [18,6,6,6,1,-1]
        Explanation: 
        - index 0 --> the greatest element to the right of index 0 is index 1 (18).
        - index 1 --> the greatest element to the right of index 1 is index 4 (6).
        - index 2 --> the greatest element to the right of index 2 is index 4 (6).
        - index 3 --> the greatest element to the right of index 3 is index 4 (6).
        - index 4 --> the greatest element to the right of index 4 is index 5 (1).
        - index 5 --> there are no elements to the right of index 5, so we put -1.
    ---------
    Example 2:    
        Input: arr = [400]
        Output: [-1]
        Explanation: There are no elements to the right of index 0.
    ---------
"""