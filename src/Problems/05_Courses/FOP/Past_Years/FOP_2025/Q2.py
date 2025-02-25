import random

"""
    Question 1 (a)
      - Time Complexity:  O(n)
      - Space Complexity: O(n)
"""
print("Question 2 (a)")
def largest_even() -> int:
    nums = []
    # Generate 10 random number
    for _ in range(10):
        num = random.randint(1, 100)
        nums.append(num)
    
    print(nums)

    even_num = 0
    # Find largest even number
    for num in nums:
        if (num % 2 == 0):
            even_num = max(even_num, num)

    return even_num
   
   
print("Largest even number: %d" %largest_even())
    