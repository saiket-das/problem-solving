def titleToNumber(columnTitle: str) -> int:
    # Store the computed column number
    column_number: int = 0

    for ch in columnTitle:
        # Convert 'A'-'Z' to 1-26
        digit_value: int = ord(ch) - ord('A') + 1
        # Base-26 accumulation
        column_number = column_number * 26 + digit_value

    return column_number

print(titleToNumber("FXSHRXW"))


"""
    -----------
    Example 1:
        Input: columnTitle = "A"
        Output: 1
    -----------
    Example 2:
        Input: columnTitle = "AB"
        Output: 28
    -----------
    Example 3:
        Input: columnTitle = "ZY"
        Output: 701
    -----------
    Example 4:
        Input: "FXSHRXW"
        Output: ?
    -----------
    Formula
    = (F * 26^6) + (X * 26^5) + (S * 26^4) + (H * 26^3) + (R * 26^2) + (X * 26^1) + (W * 26^0)
    -----------

"""