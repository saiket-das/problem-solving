# https://www.geeksforgeeks.org/problems/data-type-1666706751/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=data-type


# Data Type - Character, Integer, Long, Float and Double

def dataTypeSize(str: str) -> int:
    if (str.casefold().__eq__("character")):
        return 1
    elif (str.casefold().__eq__("float") or str.casefold().__eq__("integer")):
        return 4
    elif (str.casefold().__eq__("long") or str.casefold().__eq__("double")):
        return 8
    else:
        return -1

print(dataTypeSize("float"))
"""
    Input: Character
    Output: 1
    Explaination: For java it would be 2 bytes.
    --------
    Input: Integer
    Output: 4
"""