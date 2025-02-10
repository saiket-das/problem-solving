# Decimal number to Binary number

# Question 1 (a) -- Time Complexity: O(logN)
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

print(decimal_to_binary(10))

# Question 1 (b)  -- Time Complexity: O(5) -> O(1)
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

average: float = mark_grade()
print("Average: %.2f" %average)



"""
    Question 1 (a)
    ----------
    n = 7
    str = ""

    7 % 2 = 1, n = 3 and str = "1"
    3 % 2 = 1, n = 1 and str = "11"
    1 % 2 = 1, n = 1 and str = "111"
"""