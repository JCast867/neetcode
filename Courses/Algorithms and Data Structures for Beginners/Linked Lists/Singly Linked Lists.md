# Singly Linked Lists
A **linked list** is another data structure that is like an array in the sense that it stores elements in an ordered sequence but there are some key differences between them. The main difference is that linked lists are made up of objects called `ListNode`'s. This object contains two attributes:
1. `value` - this stores the value of the node. It could be a character, integer, etc.
2. `next` - This stores the reference to the next node in the linked list. 

## Creating a Linked List from Scratch
By chaining these `ListNode` objects together, we can build a **linked list**. We start with a `ListNode` class:
```py
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
```
Using the `next` pointer of each, we can connect the nodes together. We would have to make sure that our next pointers point to another `ListNode` and not `null`. Only the last node in the linked list would have its `next` pointer point to `null`.
```py
# the address for ListNode2 is retrieved from memory
ListNode1.next = ListNode2
```

`ListNode1`'s next pointer points to `ListNode2`. Next, we set the `next` pointer for `ListNode2` and `ListNode3`.
```py
ListNode2.next = ListNode3
ListNode3.next = None
```

## Traversal
To traverse a linked list from beginning to end, we can just make use of a simple while loop.
```py 
cur = ListNode1
while cur:
    cur = cur.next
```
1. We start the traversal at the **head** of the list, which is `ListNode1`
2. We assign it to the variable `cur`, denoting the current node we're at
3. We execute the `while` loop until we reach the end of the list which is `null`
4. In each iteration, we update `cur` to be the next node in the list by setting `cur = cur.next`
5. The traversal runs in O(n) time where *n* is the number of nodes in the linked list

### Circular Linked List
An interesting situation presents itself if `ListNode3`'s next pointer is set to `ListNode1` instead of `null`. This results in a circular linked list. Trying to iterate through a circular linked list would jusr result in an infinite loop since we'd never reach the end of the linked list.

## Operations of a Singly Linked List
Linked Lists have a `head`, and a `tail` pointer. The `head` pointer points to the very first node in the linked list, `ListNode1`, and the `tail` pointer points to the very last node, `ListNode3` in this example. If there's only one node in the Linked List, the `head` and `tail` point to the same node.

### Appending
An advantage that Linked Lists have over arrays is that inserting a new element can be performed in constant, O(1), time. Even if we insert in the middle. We don't have to shift any elements since there isn't a requirement for the elements to be stores next to each other in memory. However, if we have to traverse the list to arrive at the insertion point, the operation would take O(n) time. If we wanted to append `ListNode4` to the end of the list, we would be appending to the tail. Once `ListNode4` is appended, we update our tail pointer to be `ListNode4`. This would be done in O(1) time since it's only 1 opeation.
```py
tail.next = ListNode4
tail = ListNode4
```

### Deleting from a Singly Linked List
Deleting a node from a singly linked list will take O(1) since we can do this by updating a single pointer. This assumed we already have a reference to the node at the desired position we want to delete. If we have to traverse the list to arrive at the deletion point, the operation would take O(n) time. If we wanted to delete `ListNode2`, our `head` points to `ListNode1`, and `head.next` points to `ListNode2`. We can update our `head.next` pointer to `ListNode3`, which can be accessed by chaining `next` pointers like `head.next.next`. This makes since since `head.next` is `ListNode2`, and logically, `head.next.next` would be `ListNode3`.
```py
head.next = head.next.next
```

## Time Complexity
* Access - O(n)
* Search - O(n)
* Insertion - O(1); If you already have a reference to the node. If not, O(n)
* Deletion - O(1); If you already have a reference to the node. If not, O(n)