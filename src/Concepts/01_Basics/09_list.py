# LIST in Python

# Numbers list
numbers = [1, 3, 5, 7, 9]
print("Third element: %d" %numbers[2])
print("Last element: %d" %numbers[-1])   # Last element of the list
print(numbers)

# String list
names = ["Ahan", "Saiket", "Bilbo", "Noor", "Shojib"]
for name in names:
    print(name)
 
names[0] = "Bryan"  # [0] index value changed ("Ahan" -> "Bryan")
print(names[1:3])   # ["Saiket", "Bilbo"]


# List methods
courses = ["CM", "FOP", "CSO", "HCI"]
courses.append("ENG III")          # Append at the last index     ["CM", "FOP", "CSO", "HCI", "ENG III"]
courses.insert(3, "DS")            # Append at the specific index ["CM", "FOP", "CSO", "DS", "HCI", "ENG III"] 
print("\n%s" %courses)
print("Length: %d" %len(courses))  # 6
print("FOP" in courses)            # True (Check is 'FOP' exists or not in courses list)


# Pair List
pairs = [(1, "A"), (2, "B"), (3, "C"), (4, "D")]
for a, b in pairs:
    print("%d: %c" %(a, b))