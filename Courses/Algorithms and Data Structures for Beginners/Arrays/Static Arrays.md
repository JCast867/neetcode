# Static Arrays
In statically typed languages like Java and C++, arrays have to have an allocated size and type when initialized. These are known as static arrays. They are called static because the size of the array cannot change once declared. And once the array is full, it can not store additional elements. Some dynamically typed languages such as Python and JavaScript do not have static arrays instead they have dynamic arrays.


## Reading from an array
To read from an array, you can have it declared as `myArray = [1, 3, 5]` and we can **access** the position we want by using their indexes. So we can do `myArray[i]`. **Accessing** a single element in an array is always in *constant* time because each index in `myArray` is mapped to an address in RAM. Regardless of the size of the input array, the time taken to access an element is the same. This is referred to as *O(1)* in terms of time complexity.

### Traversing through an array
We can also read all the values in an array by traversing through them. We can traverse through `myArray` using a `for` loop or a `while` loop. To traverse through an array of size *n*, the time complexity is *O(n)*. This means the number of operations grows linearly with the size of the array. 


## Deleting from an array
### Deleting from the end of an array
In statically typed languages, all array indeces are filled with `0s` or some default value before being initialized. When we want to remove an element from the **last index** of an array, setting it to `0`/`null` or `-1` is the best we can do. This is known as a **soft delete** because the element isn't being "deleted". It's being overwritten by a value that signifies an empty index. We'll also reduce the length by `1` since we have 1 less element in the array after deleting. For example:

```py
def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0  # replacing the last value with a default value
        # should also consider the length of the array decreased by 1
```
Deleting the **last** element from an array will have a time complexity of *O(1)*.

### Deleting from an `ith` index
If we wanted to delete an element at a random index `i`, we could naively just replace it with `0`. But this would break the contiguous nature of our array. Deleting from the end won't make it non-contiguous, but deleting from the middle will. Instead, we'd have to be given the index that should be deleted `i`, we iterate starting from `i + 1` until the end of the array, we shift each element `i` position to the left, and then replace the last element with a `0` or `null` to mark it empty and decrease the length by `1`. For example:

```py
def removeMiddle(arr, i, length):
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
        # no need to remove arr[i] since we already shifted
```
The worse case would be that we need to shift all elements to the left and this would only happen if the target index is the first element in the array. Therefore, the time complexity of **deleting from the `ith` index** is *O(n)*.


## Insertion
### Inserting at the end
If we want to insert an element at the end of an array, we can simply insert it at the next open position which will be at the index `length` where `length` is the number of elements in an array. For example:

```py
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n
```
Since we are writing a single value to the array, the time complexity will be *O(1)*.

### Inserting at the `ith` index
Inserting at a more complicated index `i` is more involved since we may insert in the middle of the array. Consider the array `[4, 5, 6]`, if we need to insert at index `i = 1` or `i = 0`, we can't just overwrite the original value because we would lose it. Instead, we'd have to shift all the values. Starting at index `i`, one position to the right. For example:

```py
def insertMiddle(arr, i, n, length):
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]

    arr[i] = n
```
The time complexity for this will be *O(n)*.