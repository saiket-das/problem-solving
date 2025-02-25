def multiply_nums(n):
    # Initialize an empty list to store unique multiples of 3 and 5
    sum_list = []

    # Iterate through multiples of 3 and add them to sum_list
    for i in range(0, n, 3):
        sum_list.append(i)
    
    # Iterate through multiples of 5
    for i in range(0, n, 5):
        # Ignore values that are already added (to avoid duplicates)
        if i in sum_list:
            continue
        sum_list.append(i)

    # Calculate and print the total sum of unique multiples of 3 and 5
    print(sum(sum_list))


multiply_nums(100)