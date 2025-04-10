# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/


from collections import defaultdict

"""
    Brute Force: HashMap
        TC: O(n + m) + O(n + m) + O(n + m)
        TC: O(n + m) + O(n + m)
"""

# Function to update a dictionary with the count and sum of indices for each unique value
def update_index_sum(index_sum_dict, value, index):
    # If value not in dictionary, initialize with count 1 and sum as index
    if value not in index_sum_dict:
        index_sum_dict[value] = {"count": 1, "sum": index}
    else:
        # Update count and sum if value already exists
        previous_index_sum = index_sum_dict[value]["sum"]
        index_sum_dict[value] = {"count": 2, "sum": previous_index_sum + index}


def brute_force(list1: list[str], list2: list[str]) -> list[str]:
    # Dictionary to store the sum of indices and count for each element
    index_sum_dict = {}

    # Initial indices for both lists
    i, j = 0, 0
    len1, len2 = len(list1), len(list2)

    # Traverse both lists and update the dictionary with index sums
    while i < len1 or j < len2:
        if i < len1:
            update_index_sum(index_sum_dict, list1[i], i)
            i += 1
        
        if j < len2:
            update_index_sum(index_sum_dict, list2[j], j)
            j += 1
    
    # Find the minimum sum of indices for values that appear in both lists
    min_index_sum = float('inf')
    for _, value in index_sum_dict.items():
        if value["count"] == 2:
            min_index_sum = min(value["sum"], min_index_sum)
    
    # Collect values that have the minimum index sum
    common_elements = []
    for key, value in index_sum_dict.items():
        if value["count"] == 2 and min_index_sum == value["sum"]:
            common_elements.append(key)
    
    return common_elements



# Main function
def findRestaurant(list1: list[str], list2: list[str]) -> list[str]:
    print(brute_force(list1, list2))




findRestaurant(["happy","sad","good"], ["sad","happy","good"])                                # ["sad","happy"]
findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
               ["KFC","Shogun","Burger King"])                                                # "Shogun"
findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], 
               ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])    # "Shogun"