## QuickSort

QuickSort is a **divide and conquer** sorting algorithm that selects a pivot element, partitions the array, and recursively sorts the subarrays.

#### How QuickSort Works

1. **Choose a Pivot**: Select an element as the pivot (e.g., first, last, or random element).
2. **Partition**: Rearrange the array so elements smaller than the pivot are on the left and larger elements are on the right.
3. **Recursively Sort**: Apply QuickSort on the left and right subarrays.

#### Example

**Input:** `[10, 7, 8, 9, 1, 5]`

#### **Step-by-Step Execution:**

```
Step 1: Choose pivot (e.g., last element 5) and partition
Step 2: Rearrange into [1, 5, 7, 8, 9, 10] with pivot in correct position
Step 3: Recursively apply QuickSort to left [1] and right [7, 8, 9, 10]
Step 4: Continue until fully sorted

Final Sorted Array: [1, 5, 7, 8, 9, 10]
```

#### Time Complexity

- **Best Case:** O(n log n)
- **Average Case:** O(n log n)
- **Worst Case:** O(n²) (when pivot selection is poor)

#### Space Complexity

- **O(log n)** (recursive stack usage in the best case)
- **O(n)** (worst case recursion depth)

#### When to Use QuickSort?

✅ Fast for large datasets.  
✅ **In-place sorting** (less memory usage).  
✅ Works well with **randomized pivot selection**.  
❌ Not stable (relative order of equal elements may change).  
❌ Poor pivot selection can lead to worst-case O(n²) complexity.
