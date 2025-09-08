# Queues
Another data structure that overlaps with arrays is a Queue. They're also similar to stacks, except they follow a FIFO approach (First In First Out)

## Implementation and Operations
The easiest way to implement a queue is using a linked list. It's possible to implement a queue using a dyna,ic array, but is more involved. To get the same time complexity as a linked list, you would need to use a circular array and perform some additional operations. The main two operations that queues support are `enqueue` and `dequeue`.

### Enqueue
The **enqueue** operation inserts an element to the end of the queue. If we implement this operation with a singly linked list, it runs in O(1) time.
```py
def enqueue(self, val):
    newNode = ListNode(val)

    # queue is non empty
    if self.right:
        self.right.next = newNode
        self.right = self.right.next
    # queue is empty
    else:
        self.left = self.right = newNode
```

### Dequeue
The **dequeue** operation removes an element from the front of the queue and returns that element
```py
def dequeue(self):
    # queue is empty
    if not self.left:
        return None
    
    # remove left node and return value
    val = self.left.val
    self.left = self.left.next
    if not self.left:
        self.right = None
    return val
```
Similar to stacks, it's a good measure to check if the queue is empty before performing the dequeue operation. There is also a variation of the queue, a double-ended queue, known as a **deque**. A deque allows you to add and remove elemenrs from both the head and the tail in O(1) time. One of the most important use cases for the queue is when performing breadth-first search for trees and graphs.

## Time Complexity
* Enqueue - O(1)
* Dequeue - O(1)
