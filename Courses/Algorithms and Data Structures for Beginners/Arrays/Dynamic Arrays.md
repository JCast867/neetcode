# Dynamic Arrays
Dynamic Arrays are a more common alternative to static arrays. They're useful because the can grow as elements are added. In JavaScript and Python, these are the default arrays. Unlike static arrays, with dynamic arrays we don't have to spedicy a size uopn initialization.

## Dynamic Array Insertion
When inserting at the end of a dynamic array, the empty space is found and the element is inserted there. For example:

```py
# insert n in the last position of the array
def pushback(self, n):
    if self.length == self.capacity:
        self.resize()

    # insert at next empty position
    self.arr[self.length] = n
    self.length += 1
```

## Resize
Somce the array is dynamic in size, we can keep on adding elements. This can be done by copying over the values to a new static array that is double the size of the original. For example:

```py
def resize(self):
    self.capacity = 2 * self.capacity
    newArr = [0] * self.capacity

    for i in range(self.length):
        newArr[i] = self.arr[i]
    self.arr = newArr
```
Adding elements to a dynamic array runs in O(1) **amortized** time. Amortized time complexity is the average time taken per operation over a sequence of operations. The resize operation itself is O(n), but since it isn't performed every time we add an element, the average time taken per operation is O(1). But this is only the case if we double the size of the array when we run out of space.

### Why double the capacity
To analyze the time complexity we have to take into consideration the **sum of all the operations** that occured before the last one since we would not have gotten to the resulting array without these operations. To achieve an array of size `8`, we would have to perform `1+2+4+8=15` operations, which includes the resize operations. The pattern here is that the last term (the dominating term) is always greater than or equal to the sum of all the terms before it. In this case, `1+2+4=7`, and `7<8`. Add in the `8` to the `7`, we get a total of `15` operations to create the resulting array of size `8`. Generally, the formula is that for any array size `n`, it will take at most `2n` operations to create, which would belong to *O(n)*.

### Other Operations
Inserting or removing from the middle of a dynamic array would be similar to a static array. We'd have to shift elements to the right or left to make space for the new element or to fill the gap left by the removed element. This would run in *O(n)* time.

## Time Complexity
**Access** = *O(n)*

**Insertion** = *O(1)*; if inserting in the middle shifting, will be required which will make it *O(n)*

**Deletion** = *O(1)*; if deleting in the middle shifting, will be required which will make it *O(n)*