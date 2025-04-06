# https://codeforces.com/gym/518277/problem/A

# ** Wrong Solution ** 
def solve_kfc_countdown(k, c, secret_numbers):
    # Create initial array of chickens (1-indexed for easier position tracking)
    chickens = list(range(1, c + 1))
    
    while True:
        # Find positions to remove (convert to 0-indexed)
        positions_to_remove = [pos - 1 for pos in secret_numbers if pos <= len(chickens)]
        
        # If no valid positions to remove, we're done
        if not positions_to_remove:
            break
        
        # Remove the chickens at these positions (in reverse order to maintain indices)
        positions_to_remove.sort(reverse=True)
        for pos in positions_to_remove:
            if pos < len(chickens):  # Ensure position is valid
                chickens.pop(pos)
    
    return len(chickens)


# Main function
def main():
    # Number of test cases
    t = int(input())
    
    for _ in range(t):
        # `K` = Number of secrets and `C` = Number of chickens
        k, c = map(int, input().split())
        # Read the `K` Secret numbers
        secret_numbers = list(map(int, input().split()))
        
        result = solve_kfc_countdown(k, c, secret_numbers)
        print(result)

if __name__ == "__main__":
    main()