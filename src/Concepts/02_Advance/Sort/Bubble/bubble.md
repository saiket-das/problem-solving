## Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares `adjacent` elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

#### How Bubble Sort Works

1. Start at the first element of the array.
2. Compare the current element with the next one.
3. If the current element is greater than the next one, swap them.
4. Move to the next element and repeat steps 2-3 for the rest of the array.
5. After one full pass, the largest element will be at the end.
6. Repeat the process for the remaining unsorted elements (excluding the last sorted elements).
7. Continue until no swaps are needed, meaning the array is sorted.

#### Example

**Input:** `[5, 3, 8, 4, 2]`

### **Step-by-Step Execution:**

```
Pass 1: [5, 3, 8, 4, 2]
        [(5, 3), 8, 4, 2]  -> [3, 5, 8, 4, 2]  Swap (3, 5)
        [3, (5, 8), 4, 2]  -> No swap
        [3, 5, (8, 4), 2]  -> [3, 5, 4, 8, 2]  Swap (4, 8)
        [3, 5, 4, (8, 2)]  -> [3, 5, 4, 2, 8]  Swap (2, 8)

Pass 2: [3, 5, 4, 2, 8]       Ignore 8 (Already sorted)
        [3, (5, 4), 2, 8]  -> [3, 4, 5, 2, 8]  Swap (4, 5)
        [3, 4, (5, 2), 8]  -> [3, 4, 2, 5, 8]  Swap (2, 5)

Pass 3: [3, 4, 2, 5, 8]       Ignore 5 and 8
        [3, (4, 2), 5, 8]  -> [3, 2, 4, 5, 8]  Swap (2, 4)

Pass 4: [3, 2, 4, 5, 8]       Ignore 4, 5 and 8
        [(3, 2), 4, 5, 8]  -> [2, 3, 4, 5, 8]  Swap (2, 3)

Final Step: [2, 3, 4, 5, 8]  (Sorted)
```

#### Time Complexity

- **Best Case (Already Sorted):** O(n)
- **Average Case:** O(n²)
- **Worst Case (Reverse Sorted):** O(n²)

#### Space Complexity

- **O(1)** (In-place sorting, no extra space used)

#### When to Use Bubble Sort?

✅ When simplicity is more important than efficiency.
✅ When the input is **almost sorted** (Best case O(n)).
❌ Not ideal for large datasets due to O(n²) complexity.
