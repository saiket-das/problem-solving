# https://www.naukri.com/code360/problems/allocate-books_1090540?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries


"""
    Bianry Search
        TC: O(log sum(arr) * n)
        SC: O(1)
"""
def studentCount(arr: list[int], pages: int) -> int:
    student_count, current_page_sum = 1, 0

    for page in arr:
        if current_page_sum + page <= pages:
            # Add the page to the current student’s total
            current_page_sum += page
        else:
            # Allocate a new student if the current student exceeds the page limit
            student_count += 1
            # Start the new student with the current page
            current_page_sum = page
    
    return student_count


def findPages(arr: list[int], m: int) -> int:
    low = max(arr)     # The minimum possible maximum pages is the largest book
    high = sum(arr)    # The maximum possible maximum pages is the total sum of all pages

    while low <= high:
         # `mid` value as a potential max page limit
        mid = (low + high) // 2
        
        # If more than 'maxStudents' are required, increase the max page limit
        if studentCount(arr, mid) > m:
            low = mid + 1
        else:
            # If within the limit, try a smaller max page limit
            high = mid - 1
    
    # 'low' will be the smallest maximum page limit that works
    return low


print(findPages([1,2,3,4,5], 2))     # 9 [4, 5]
print(findPages([7,2,5,10,8], 2))    # 18 [10, 8]