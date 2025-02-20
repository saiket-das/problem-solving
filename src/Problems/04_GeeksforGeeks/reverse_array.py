# Reverse an Array using Recursion 

# Using Two Pointer
def reverse_array(left: int, right: int, arr: list):
    if left >= right:
        return
    # Swap elements without using a temp variable
    arr[left], arr[right] = arr[right], arr[left]
    # Recursive call
    reverse_array(left + 1, right - 1, arr)


nums = [1, 2, 3, 4, 5]
print("Before Reverse:", nums)    # [1, 2, 3, 4, 5]
reverse_array(0, len(nums)-1, nums)
print("After Reverse:", nums)     # [5, 4, 3, 2, 1] 


# ----------------------
# Reverse Array without Two Pointer
def reverse_array_2 (arr: list[int], i: int , n: int):
    if (i >= (n/2)):
        return 
    # Swap values
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

    # Call recursion function with (l+1, r-1)
    return reverse_array_2(arr, i + 1, n)

nums_2: list[int] = [11, 22, 33, 44, 55]
print("Before Reverse")
print(nums_2)    # [11, 22, 33, 44, 55] 
reverse_array_2(nums_2, 0, len(nums_2))
print("After Reverse")
print(nums_2)    # [55, 44, 33, 22, 11] 
