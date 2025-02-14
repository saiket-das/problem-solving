# CONDITION in Python (if-else, switch)

# If Else
temperature: int = -5

if temperature < 20:
    # To print both statements on the same line, we can use the end=" " argument in print(), or use sep="" for concatenation.
    print("Cold: %d° Celcius" %temperature, end = " ", sep = " ")
    if temperature <= 0:
        print("Frozen")
elif temperature < 30:
    print("Warm: %d° Celcius" %temperature)
else:
    print("Very Hot: %d° Celcius" %temperature)


 

# Weight converter program
print("\n--- Weight Converter ---")
weight = float(input("Enter your weight: "))
unit = input("(K)g or (L)bs: ")

if (unit.upper().__eq__ ('K')):
    print("\nWeight in Lbs: %.2f" % (weight * 2.20))
elif (unit.upper().__eq__ ('L')):
    print("\nWeight in Kg: %.3f" % (weight / 2.20))
else:
    print("\nWrong input. Enter (K or L)")



# Mark to Grade (using if-else)
print("\n\n--- Mark to Grade Converter ---")
mark: int = int(input("Enter your mark: "))

if  (80 <= mark <= 100):
    print("Grade: A+")
elif (70 <= mark <= 79):
    print("Grade: A")
elif (60 <= mark <= 69):
    print("Grade: B")
elif (50 <= mark <= 59):
    print("Grade: C")
elif (40 <= mark <= 49):
    print("Grade: D")
elif (0 <= mark <= 39):
    print("Grade: F")
else:
    print("Invalid input. Enter mark between 0 to 100.")


markTens = mark // 10  # Get the tens digit
match markTens:
    case 10 | 9 | 8:
        print("Grader (using Switch): A+")
    case 7:
        print("Grader (using Switch): A")
    case 6:
        print("Grader (using Switch): B")
    case 5:
        print("Grader (using Switch): C")
    case 4:
        print("Grader (using Switch): D")
    case 0 | 1 | 2 | 3:
        print("Grader (using Switch): F")
    case _:
        print("Invalid input. Enter mark between 0 to 100.")
