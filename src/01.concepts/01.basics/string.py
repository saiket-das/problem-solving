# STRING in Python

course: str = "Fundmentals Of Programming"
# {'F', 'u', 'n', 'd', ...}


print(course.upper())
print(course.lower())
print(course)

# caseFold to ignore case sensitive
print(course.casefold().find('program'))
print("of" in course.casefold())  # True or False (If 'of' contains in Course String)

print(course.replace("of", "Of"))