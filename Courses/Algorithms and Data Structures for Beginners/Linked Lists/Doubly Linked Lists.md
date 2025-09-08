# Doubly Linked Lists
In **Doubly Liked Lists**, each node has two pointers now. In addition to the `next` pointer, we have a `prev` pointer which points to the previous node. If the `prev` pointer points to `null`, then we are at the head of the linked list.

## Operations of Doubly Linked Lists
### Insetion End
Similar to the singly linked list, adding a node to a doubly linked list will run in O(1) time. Only this time, we'll have to update the `prev` pointer as well. For example, if we have three nodes in our Linked list, `ListNode1`, `ListNode2`, and `ListNode3`. Now we have another node, `ListNode4`, that we wish to insert at the end. We will have to update both the `next` pointer of `ListNode3` and the `prev` pointer of `ListNode4`
```py
tail.next = ListNode4
ListNode4.prev = tail
tail = tail.next
```

### Insertion Front
Since we have references to the nodes, this will be done in O(1) time. 
```py
ListNode4.next = head
ListNode4.prev = None
head.prev = ListNode4
head = ListNode4
```

### Deletion End
Deleting at the end is also a O(1) operation.
1. We get the reference to the node before the tail
2. We update the `next` pointer of the node before the tail to `null`
3. We update the tail to be the node before the tail
4. (Optional) We can also update the `prev` pointer of the old tail to `null`
```py
ListNode2 = tail.prev
ListNode2.next = null
tail = ListNode2
```

### Deletion Front
Deleting from the front is also a O(1) operation.
```py 
head.next.prev = null
head = head.next
```

### Access
The same to singly linked lists, we can't randomly access a node. So the worst case would be O(n) since it'll have to traverse the whole list. One thing to note is that in doubly linked lists, you can traverse in both directions. As oppose to singly linked lists.

## Time Complexity
* Access - O(n)
* Search - O(n)
* Insertion - O(1); If you have a reference to the desired node. If not, O(n)
* Deletion - O(1); If you have a reference to the desired node. If not, O(n)
