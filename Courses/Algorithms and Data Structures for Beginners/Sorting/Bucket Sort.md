# Bucket Sort
Bucket Sort works well when the dataset to be sorted has values **within a specific range**. It's not as popular or widely used as other sorting algorithms.

## Concept
Imagine we have an array of size 6 and it contains values of an inclusive range 0-2. The idea behind bucket sort is to create a "bucket" for each one of the numbers and map them to their respective buckets.

There will be a bucket for 0, 1, and 2. This bucket, which is just a position in a specified array will contain the frequencies of each one of the values within the range. For the sake of this example, we only have three values and accordingly we will have three buckets. The term bucket will really just translate into a position in an array where we will map these frquencies

Once each one of the buckets is filled with the frequency of each one of the values, we will overwrite all the values in the original array such that they end up in the sorted order
```py
def buckerSort(arr):
    # assuming arr only contains 0, 1, or 2
    counts = [0, 0, 0]

    # count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr
```
The first part, right before we do `i = 0`, corresponds to filling up each one of the buckets. For the second part:
* The `i` pointer will keep track of the next insertion position for our original array, `arr`
* The `n` pointer keeps track of the current position of the `counts` array
* The `j` pointer keeps track of the number of times that `counts[n]` has appeared

So, knowing that we have our `counts` array which is `[2, 1, 3]`. And our original input array is `[2, 1, 2, 0, 0, 2]`. At the first iteration, n = 0, which corresponds to 2 in `counts`. Our inner loop will run two times, overwriting `arr[0]` and `arr[1]` to be `0`. This makes perfect sense because we had two zerps and putting them in `arr` in an adjacent manner will result in them being sorted. This process will continue for each number and the ultimate state of `arr` will be `[0, 0, 1, 2, 2, 2]` which is the ultimate goal

## Time Complexity
Although there is a nested loop, it's not O(n^2). We know that for the first for loop, we are performing n steps since we are going through all the elements and counting frequency. The first for loop will run n times where n is the length of the `counts` array. However, the inner lop will only run until `counts[n]`, which is different everytime. The first time it will be 2, then 1, and then 3. Therefore, our algorithm belongs to O(n)

## Stability
Since we are overwriting the original array, there's no way to preserve the relative order of the values. There's no swapping that takes place either. Hence, it will stay unstable