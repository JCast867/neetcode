# Insertion Sort
Insertion sort is one of many sorting algorithms used to sort data in different data structures. It's a simple algorithm that is easy to implement and understand. However, it's not the most efficient algorithms when it comes to large data sets.

## Concept
Given an array `[2, 3, 4, 1, 6]`, the goal is to sort it to `[1, 2, 3, 4, 6]`. Insertion sort does this by sorting portions of the array at a time. Having an array of size 1, that's already sorted because there's no other elements to compare it with. So, we assume the first element is sorted because we treat it as its own subarray. The next subarray will be of size 2 starting from the beginning. In this example, that is `[2, 3, ...]`. To sort only these two elements, we just have to compare them. For an array of size 2, this is easy. But, when we get to the full array of size 5, there's no way to keep track of where each element is without using pointers. So let's take two pointers, `i` and `j`. 
1. The `i` pointer points at the element we are currently inserting into the sorted portion array.
2. The `j` pointer starts off one index to the left of `i`
3. Our goal is to find the position that `arr[i]` should be inserted into the sorted portion of the array
4. We continue swapping it with `arr[i]` until we find the correct position
5. After each swap, we shift `j` to the left by 1
6. We stop once the element is greater than or equal to the element to its left

```py
def insertionSort(arr):
    # traverse through 1 to the end
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
    return arr
```

## Stability
This is a stable sorting algorithm. It is guaranteed that the relative order will remain the same

## Time and Space Complexity
### Time
If the input array is already sorted, the inner loop will never execute. This is the best case scenario where time complexity is O(n)

In the worst case, the time complexity is O(n^2). This is because the inner loop will execute n times for each element in the array. This will happen if the array is in reverse order.

### Space
Insertion sort is an in-place algorithm. Meaning that the space complexity is O(1) since no additional data structures are used