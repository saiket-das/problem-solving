# Number to Binary

print("Number to Binary: ", end = "")
def number_to_binary(num: int):
    if (num < 1):
        return 1
    
    number_to_binary(num // 2)
    print("%d" %(num % 2), end = "")

number_to_binary(10)
print()