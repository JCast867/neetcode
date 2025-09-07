# Stacks
A stack is a data structure that supports a subset of operations from a dynamic array. With a stack, you can only add (push) and delete (pop) elements from one end of the array (top of the stack). Think of a stack of plates. You can't get to the middle or bottom elements. You can only touch the top element. Stacks operate using LIFO (Last In First Out). The last element added to the stack is the first element coming out. There are three operations for stack. `push`, `pop`, and `peek`.

## Push
The **push** operation add elements to the top of the stack. This is very effecient with a constant, O(1), time complexity.
```py 
def push(self, n):
    self.stack.append(n)
```

## Pop
The **pop** operation removes the last element from the top of the stack. This is also very efficient with constant, O(1), time complexity.
```py
def pop(self):
    self.stack.pop()
```
It's a good measure to check if the stack is empty before popping elements to avoid errors.

## Peek
The peek operation returns the top element without removing it. Also very effecient with constant, O(1), time complexity.
```py
def peek(self):
    return self.stack[-1]
```
