# Decimal number to Binary number

"""
    Question 1 (a)
      - Time Complexity:  O(log n)
      - Space Complexity: O(log n)
"""
def decimal_to_binary (n: int) -> int:
    binary_str: str = ""

    while (n >= 1):    # O(logN)
        # Get the remainder from number
        digit: int = n % 2
        # Save the remainder into String (binary_str)
        binary_str += str(digit)
        n //= 2

    # Reverse the String 
    binary_str = binary_str[::-1]    # O(logN)
    # Convert the Binary String to Integer and Return
    return int(binary_str)

print("Question 1 (a)")
decimal_num = int(input("Enter decimal number: "))
print("%d decimal to binary is: %d" %(decimal_num, decimal_to_binary(decimal_num)))

# --------------------------
"""
    Question 1 (b)
      - Time Complexity:  O(5) -> O(1)
      - Space Complexity: O(1)
"""
def mark_grade () -> float:
    totalMark: int = 0
    i = 0
    while (i < 5):
        mark: int = int(input("Enter your course mark %d (0 - 100): " %(i+1)))
        if not(0 <= mark <= 100):
            print("Invalid input. Enter mark between 0 to 100")
            continue
        # AppeCalculate Total course mark
        totalMark += mark
        i += 1
    
    # Calculate Average ad Return
    return totalMark / 5

print()
print("Question 1 (b)")
average: float = mark_grade()
print("Average: %.2f" %average)

# --------------------------
"""
    Question 1 (c)
      - Time Complexity:  O(1)
      - Space Complexity: O(1)
"""
def convert_to_grade(average: float):
    match (average // 10):
        case 9 | 10:
            print("Grade: A") 
        case 8:
            print("Grade: B")
        case 7:
            print("Grade: C")
        case 6:
            print("Grade: D")
        case _:
            print("Grade: F")

print()
print("Question 1 (c)")
(convert_to_grade(average))
