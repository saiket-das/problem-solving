# Hashing

def hashing(arr: list[int]) -> int:
    freq = set()

    for x in arr:
        if x in freq:
            return False
        else:
            freq.add(x)

    return True

# Check is any value Twice in Array
print(hashing([11, 11, 22, 33, 44, 55]))

# -----------

def hashing_2(arr: list[int]):
    freq_dict = {}

    for x in arr:
        freq_dict[x] = freq_dict.setdefault(x, 0) + 1
    
    # Sort the dictionary by keys
    sorted_dict = dict(sorted(freq_dict.items()))
    return sorted_dict

print(hashing_2([1, 10, 6, 9, 3, 10, 3, 3, 4, 10, 1, 6, 5, 4, 5, 7, 10, 7, 8, 10]))
