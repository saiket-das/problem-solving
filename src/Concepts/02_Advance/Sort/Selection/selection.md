## Selection Sort Algorithm

Selection Sort is a simple and intuitive sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first element of the unsorted portion.

#### How Selection Sort Works

Given an unsorted array:

```
[64, 25, 12, 22, 11]
```

The algorithm follows these steps:

1. Find the smallest element in the array and swap it with the first element.
2. Find the next smallest element and swap it with the second element.
3. Repeat the process for the remaining unsorted portion.
4. Continue until the array is completely sorted.

#### Step-by-Step Example

| Pass | Unsorted Portion       | Smallest Element | Swap Position | Array After Swap       |
| ---- | ---------------------- | ---------------- | ------------- | ---------------------- |
| 1    | `[64, 25, 12, 22, 11]` | `11`             | `0`           | `[11, 25, 12, 22, 64]` |
| 2    | `[25, 12, 22, 64]`     | `12`             | `1`           | `[11, 12, 25, 22, 64]` |
| 3    | `[25, 22, 64]`         | `22`             | `2`           | `[11, 12, 22, 25, 64]` |
| 4    | `[25, 64]`             | `25`             | `3`           | `[11, 12, 22, 25, 64]` |
| 5    | `[64]`                 | -                | -             | `[11, 12, 22, 25, 64]` |

#### Selection Sort Implementation

#### Time and Space Complexity

| Case       | Time Complexity |
| ---------- | --------------- |
| Best Case  | O(n²)           |
| Worst Case | O(n²)           |
| Average    | O(n²)           |

**Space Complexity:** O(1) (In-place sorting)

#### When to Use Selection Sort?

✅ Good for small datasets
✅ Easy to implement
❌ Not efficient for large datasets
