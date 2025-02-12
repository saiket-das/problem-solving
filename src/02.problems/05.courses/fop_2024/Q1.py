
# Question 1 (a)
def Q1_a ():
    pos, neg, zero = 0, 0, 0
    while (True):
        n = input("Enter any number: ")
        # Break loop if its "X" or "x"
        if (n == "x" or n == "X"):
            break

        # Convert to Integer
        n = int(n)
        # Count Negative, Positive, Zero numbers
        if (n < 0): neg += 1
        elif (n == 0): zero += 1
        else: pos += 1
    
    print("Positive: %d" %pos)
    print("Negative: %d" %neg)
    print("Zero: %d" %zero)

# Question 1 (b)
def Q1_b (n: int) -> int:
    sum: int = 0

    for i in range(1, n+1):
        sum += (1/i)

    return sum

Q1_a()
print("Answer: %.2f" %(Q1_b(5)))