# FUNCTION in Python

# Function pass by Reference
def function (age: int = 18, name: str = "Ahan") -> str:
    return name + ", Age: " + str(age)

print(function(45, "Saiket"))


# Pass by Value
print("\n--- Pass by Value ---")
def passedByValue(num: int) -> int:
    num += 5
    print("Inside function: %d" %num)    # 15
    return num

num: int = 10
print(passedByValue(num))    # 15 (Send a copy value of Num, not original value)
print("Outside function: %d" %num)    # 10


# Pass by Reference
print("\n\n--- Pass by Value ---")
def passedByRef(value):
    value["num"] = 20
    print("Inside function: %d" %value["num"])    # 15
    return value

value: int = {"num" : 10}
print("Before modify: %d" %value["num"])       # 10 (Before modfiy)
passedByRef(value)   # (Send a original value of Num)
print("Outside function: %d" %value["num"])    # 15 (After modfiy))