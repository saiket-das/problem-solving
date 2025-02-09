#  SET in Python

# Note: Set items are unchangeable, but you can remove items and add new items.
sets = {"Apple", "Banana", "Cherry"}
# set[0] = "Grape" (Cant perfome this)

sets.add("Grape")

# Note: Sets cannot have two items with the same value. (Duplicate values will be ignored)
sets.add("Apple")    


# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates
sets.add(True)
sets.add(1)

# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates
sets.add(False)
sets.add(0)

# To remove an item in a set, use the remove(), or the discard() method.
# Note: If the item to remove does not exist, remove() will raise an error.
sets.remove("Banana")
# Ensure the correct capitalization is used when removing an item. It should be "Banana" instead of "banana".
# sets.remove("banana")    # # KeyError: "banana" not found in the set

print(sets)

set1 = {1, 2, 3}
set2 = {"One", "Two", "Three"}

set3 = set1.union(set2)
print("\n",set3)

