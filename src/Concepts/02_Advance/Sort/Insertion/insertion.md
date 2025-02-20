## Insertion Sort

Insertion Sort is a simple sorting algorithm that builds the sorted array one element at a time by repeatedly inserting the current element into its correct position.

#### How Insertion Sort Works

1. Start with the second element (index 1) and compare it with the previous elements.
2. If the current element is smaller, shift the larger elements to the right.
3. Insert the current element in its correct position.
4. Repeat for all elements until the array is sorted.

#### Example

**Input:** `[5, 3, 8, 4, 2]`

#### **Step-by-Step Execution:**

```
Pass 1: [5, 3, 8, 4, 2]
        Insert (3) in the correct position -> [3, 5, 8, 4, 2]

Pass 2: [3, 5, 8, 4, 2]
        Insert (8) in the correct position -> No change [3, 5, 8, 4, 2]

Pass 3: [3, 5, 8, 4, 2]
        Insert (4) in the correct position -> [3, 4, 5, 8, 2]

Pass 4: [3, 4, 5, 8, 2]
        Insert (2) in the correct position -> [2, 3, 4, 5, 8]

Final Step: [2, 3, 4, 5, 8]  (Sorted)
```

#### Time Complexity

- **Best Case (Already Sorted):** O(n)
- **Average Case:** O(n²)
- **Worst Case (Reverse Sorted):** O(n²)

#### Space Complexity

- **O(1)** (In-place sorting, no extra space used)

#### When to Use Insertion Sort?

✅ When the input is **small or nearly sorted** (Best case O(n)).  
✅ When a **stable sort** is required.  
❌ Not ideal for large datasets due to O(n²) complexity.
