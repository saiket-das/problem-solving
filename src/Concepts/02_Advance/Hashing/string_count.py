def string_count(str: str):
    # chr(i + ord('a')) converts 0 to 'a', 1 to 'b', ..., 25 to 'z'
    # Dictionary initializes each letter with 0 count
    freq_dict = {chr(i + ord('a')): 0 for i in range(26)}

    for ch in str:
        # Increment count
        freq_dict[ch] += 1

    return freq_dict

result = string_count("xjvhafpudm")
print(result)