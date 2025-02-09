# LOOP in Python (for, while, do-while) 

# While loop
i: int = 1
while i <= 10:
    if i % 2 == 0:
        print(i, end = " ")
    i += 1

print(sep = " ")


# For Loop
for i in range(1, 11):
    print(i, end = " ")   # 1 - 10


numbers = [2, 3, 1, 5, 8, 11, 10]
# Using for loop
print("\n\nUsing for loop:")
for number in numbers:
    print(number, end = " ")

# Using while loop
print("\n\nUsing while loop:")
j: int = 0
while j < len(numbers):
    print(numbers[j], end = " ")
    j += 1