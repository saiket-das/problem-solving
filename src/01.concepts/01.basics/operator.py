# Arithmetic Operators (+ - * /)

print(20 + 10)   # 20
print(20 - 10)   # 10
print(20 * 10)   # 200
print(20 ** 2)   # 200 (** Means 20^2 = 400)
print(20 // 10)  # 2 (Return Integer number)
print(20 / 10)   # 2.0 (Return Float number)
print(20 % 10)   # 0
   
# Augmented Assignment Operators (+=, -+, *=, **=, /=, //=, %=)
x = 2
x += 3 # Increment
print(x)

# Operator Precedence (Same as Math)
print(10 + 3 * 2)    # 16
print((10 + 3) * 2)  # 26

# Comparison Operator (<, >, <=, >=, ==, !=)
print(10 == 2)   # False
check: bool = (3 ** 3) == (9 * 3)
print(check)     # True

# Logical Operators (or, and, not)
price: int = 25
print(price >= 10 or price <= 20)     # True
print(price >= 10 and price <= 20)    # False
print (not price > 50)                # True (Inverse operator)





