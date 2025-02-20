## Merge Sort

Merge Sort is a **divide and conquer** sorting algorithm that splits an array into smaller subarrays, sorts them individually, and then merges them back together.

#### How Merge Sort Works

1. **Divide**: Split the array into two halves recursively until each subarray contains a single element.
2. **Conquer**: Sort each half individually.
3. **Merge**: Combine the sorted halves back together in a sorted order.

#### Example

**Input:** `[5, 3, 8, 4, 2]`

#### **Step-by-Step Execution:**

```
Step 1: Divide [5, 3, 8, 4, 2] into [5, 3] and [8, 4, 2]

Step 2: Divide [5, 3] into [5] and [3]
Step 3: Divide [8, 4, 2] into [8] and [4, 2]
Step 4: Divide [4, 2] into [4] and [2]

Step 5: Merge [5] and [3] -> [3, 5]
Step 6: Merge [4] and [2] -> [2, 4]
Step 7: Merge [8] and [2, 4] -> [2, 4, 8]
Step 8: Merge [3, 5] and [2, 4, 8] -> [2, 3, 4, 5, 8]

Final Sorted Array: [2, 3, 4, 5, 8]
```

#### Time Complexity

- **Best Case:** O(n log n)
- **Average Case:** O(n log n)
- **Worst Case:** O(n log n)

#### Space Complexity

- **O(n)** (Requires additional space for merging)

#### When to Use Merge Sort?

✅ Efficient for large datasets.  
✅ When **stability** and **consistent performance** are required.  
✅ Works well for **linked lists** due to efficient merging.  
❌ Not ideal for in-place sorting due to **extra space usage**.
