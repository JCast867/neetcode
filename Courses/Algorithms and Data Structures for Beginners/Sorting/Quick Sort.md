# Quick Sort
Quick sort is another divide and conquer algorithm used for sorting, similar to merge sort

## Implementation
The idea behind quicksort is to pick an index, which is called the `pivot`. We then partition the array such that every value to the left is less than or equal to the `pivot` and every value to the right is greater than the pivot. 

### Picking a pivot value
There are several ways to pick a pivot value. Some common ways are:
* Pick the first index
* Pick the last index
* Pick the median
* Pick a random pivot

Ideally, we can pick a pivot that'll divide the array into two roughly equal halves. This would result in the most efficient sorting scenario

### Recursive partitioning
1. Once we pick a pivot, we will partition the array as such that all elements less than or equal to the pivot or on the left and the rest are on the right
2. We will then recursively run quicksort on the left and right halves until we hit the base case which is an array of size `1`

Unlike merge sort, there's no need to merge the two halves because the partitioning step itself is enough to sort the array. In some sense, quick sort is the opposite of merge sort. Merge sort has a simple recursive step, but the complexity is in handling the merging of two halves. Quick sort has a complex recursive step, but the complexity is in the partitioning step. 

### Performing a partition
Let's consider the array `[6, 2, 4, 1, 3]`. We will have sorted the array such that all elements to the left are smaller than the `pivot` with the rest being on the right. 
```py
def quickSort(arr: list[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s  # pointer for the left side

    # partition elements smaller than pivot on the left
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # move pivot between left and right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # quick sort left side
    quickSort(arr, s, left - 1)

    # quick sort right side
    quickSort(arr, left + 1, e)

    return arr
```

## Time and Space Complexity
The analysis of quicksort is similar to merge sort. The partition step takes O(n) time and we do this at every level of the recursion tree. The number of levels in the recursion tree is O(log n), but only in the best case

The best case is that we pick a `pivot` such that we can always perform the partition in the middle. If the array is perfectly partitioned in the middle every single time and the pivot is the median, it is possible to keep getting O(n log n) as the ultimate result.

Continuously picking a pivot where the `pivot` element is the smallest or biggest element will result in the worst case performance of O(n^2). This is because our partitioning will not be affective and we will end up with a partition of size `n - 1` and `0`, making the height of our tree `n`

## Stability
Quick Sort is not a stable algorithm. Take the array `[7,3,7,4,5]` where we have two 7s, one at the 0th index and one at the 2nd index. In this case, if our pivot is the 4th and the last index, we will end up with `[3,4,7,7,5]` where the 7 from the 0th index is now at 3rd index, which means that the relative order of the 7's has been reversed.
