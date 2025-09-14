# Merge Sort
Merge sort is a very common sorting algorithm that is used by many programming languages as a part of their standard libraries. The concept is very simple. Keep splitting the array into halves until the subarrays hit a size of one. Then recursively sort the subarrays by merging two subarrays at a time. The final array will be fully sorted. This is a technique knows as **divide and conquer**. Dividing the problem into smaller subproblems, solve them, and then combine the solutions to get the final answer. This is a two-branch recursion, similar to the fibonacci sequence.

## Implementation
Let's take an array of size 5 as an example, `[3, 2, 4, 1, 6]`. We want to sort it in an increasing, or non-decreasing order if we had duplicates. We will be splitting the array like this:
```
                [3, 2, 4, 1, 6]
                /               \
            [3, 2, 4]           [1, 6]
            /       |           |       \
        [3, 2]      [4]         [1]     [6]
        /    \
    [3]     [2]
```
```py
def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    # middle index
    m = (s + e) // 2

    # sorting left half
    mergeSort(arr, s, m)

    # sorting right half
    mergeSort(arr, m + 1, e)

    # merge sorted halfs
    merge(arr, s, m, e)

    return arr
```
1. We have a base case where if the length of the array is less than or equal to 1, we return the array because it's already sorted
2. Otherwise, we calculate the middle index of the array
3. We recursively call `mergeSort()` on the left half of the array. We do this by passing the pointers `s` and `m` to the function, which in this case represents the start and end of the left half of the array
4. We recursively call `mergeSort()` on the right half of the array. We do this by passing the pointers `m + 1` and `e` to the function, which in this case represents the start and end of the right half of the array
5. We merge the two sorted halves by calling `merge()` function

## Visualization and Pseudocode
### The `mergeSort()` recursive call
As we learned with two branch recursion, we solve both of the branches and 'piece' back together the solutions to the subproblems to arrive at the ultimate solution. Once we have a subarray `[3, 2]` sorted to `[2, 3]` - this is the `mergeSort(arr, s, m)` part. It's important to note the sequence in which calls are executed. The `merge()` call will not be executed until both recursive `mergeSort()` calls have returned for the current subarray. 

### The `merge()` function and three pointers
We have three pointers, `k`, `j`, and `i`
* `k` keeps track of where the next element in `arr` needs to be placed
* `i` points to the element in the `leftSubarray` that is currently being compared to the `j` element in the `rightSubarray`
* One of `i` and `j` will increment depending on which element is smaller
* `k` will increment regardless because `arr` will have an element placed inside of it regardless of which one of `i` or `j` increments
```py
def merge(arr, s, m, e):
    # copy the sorted left and right halfs to temp arrays
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i = 0  # index for L
    j = 0  # index for R
    k = s  # index for arr

    # merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # one of the halves will have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] > R[j]
        j += 1
        k += 1
```

## Time and Space Complexity
### Time
Merge Sort runs in O(n log n). If n is the length of our array at any given level, our subarrays in the next level have a length of n/2. From our example, we go from n = 4 to n = 2 to n = 1 which is the base case. The question is how many times can we divide n by 2 until we hit the base case. This would look like n/2^x = 1 where x is the number of times we need to divide n by 2 until we get to one.

1. n/2^x = 1
Isolate n by multiplying both sides by 2^x
2. n = 2^x
To solve for x, take log of both sides
3. log n = log2^x
According to log rules, we can simplify this to:
4. log n = x log 2
log 2 is basically asking 2 to the power of what is equal to 2, i.e.m 2^? = 2? 1
5. log n = x
Thus the final answer is x = log n

This means that we have log n levels in our recursion tree. But what is the cost at each level? This is dependent on the `merge()` function. Merge will take n steps because at any level of the tree, we have n elements to compare and sort, where n is the length of the original array. To get the time complexity we multiply the number of levels in the recursion tree by the cost of each level. This results in an O(n log n) time complexity

### Space
The height of the recursion tree is log n and at each level. At any given level, we have n elements to sort, which we will allocate temporary arrays for the `merge()` function. To get the total space complexity, we sum both terms and get O(n + log n) which simplifies to O(n). The reason we sum rather than multiply is because not all temporary arrays will be alocated at the same time, but rather one at a time

### Stability
Merge Sort proves to be a **stable** algorithm because if we have a pair of duplicates, say 7, the 7 in the left subarray will always end up in the merged array first followed by the 7 in the right subarray. This is because we compare the `ith` element in the left subarray to the `jth` element in the right subarray for equality, we pick the left subarray, maintaining the relative order. Recall the pseudocode from `merge()` routine.
```py
if leftSubarray[i] <= rightSubarray[j]:
    arr[k] = leftSubarray[i]
    i += 1
```