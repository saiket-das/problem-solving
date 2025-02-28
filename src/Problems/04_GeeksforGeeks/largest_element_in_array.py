# https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-element-in-array


"""
    Time Complexity:  O(n)
    Space Complexity: O(1)
"""

def largest(arr):
    # Initialize with the smallest possible value
    large = arr[0]
    for num in arr:
        # Update largest if the current number is greater
        large = max(large, num)
    
    return large

print(largest([1, 8, 7, 90, 56, 17]))