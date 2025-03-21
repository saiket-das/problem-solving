# https://leetcode.com/problems/merge-intervals/description/



"""
    Optimal: Sort
        Time Complexity: O(n log n) + O(n)
        Space Complexity: O(n)
    
    `n` = The number of Intervals
"""
def optimal(intervals: list[list[int]]) -> list[list[int]]:
    # Sort intervals based on the starting value
    intervals.sort()

    # Stores the merged intervals
    merged_intervals = []
    # Index to track the last merged interval
    merged_index = 0


    for i, (start, end) in enumerate(intervals):
        # Initialize with the first interval
        if i == 0:
            merged_intervals.append([start, end])
        # Merge overlapping intervals by updating the end time
        elif start <= merged_intervals[merged_index][1]:
            merged_intervals[merged_index][1] = max(merged_intervals[merged_index][1], end)
        # Add a new non-overlapping interval
        else:
            merged_index += 1
            merged_intervals.append([start, end])
    
    return merged_intervals


def merge(intervals: list[list[int]]) -> list[list[int]]:
    print(optimal(intervals))


merge([[1,4],[4,5]])                   # [[1,5]]
merge([[1,4],[2,3]])                   # [[1,4]]
merge([[1,3],[2,6],[8,10],[15,18]])    # [[1,6],[8,10],[15,18]]
merge([[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]])  
