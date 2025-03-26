# https://leetcode.com/problems/reverse-vowels_set-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75


"""
    Time Complexity:  O(n) + O()
    Space Complexity: O(n)
"""
def solution (s: str) -> str:
    # Define a set of vowels_set for quick lookup
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # Convert string to a list to allow mutation
    char_list = list(s)

    # Two-pointer approach: left (l) starts at beginning, right (r) at end
    left, right = 0, len(s) - 1
    
    while left < right:
        # Swap vowels
        if char_list[left] in vowels_set and char_list[right] in vowels_set:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
        # Move right pointer leftward if right character is not a vowel
        elif char_list[left] in vowels_set:
            right -= 1
        # Move left pointer rightward if left character is not a vowel
        elif char_list[right] in vowels_set:
            left += 1
        # Move both pointers if neither character is a vowel
        else:
            left += 1
            right -= 1

    return "".join(char_list)

def reversevowels_set(s: str) -> str:
    print(solution(s))


reversevowels_set("IceCreAm")    # "AceCreIm"
reversevowels_set("leetcode")    # "leotcede"