# Depth-First Search
Depth First Search (DFS) is one of the most common algorithms in coding interviews. It is commonly used to traverse trees and graphs. If we want to traverse an entire tree, we have to visit every node. One way to accomplish this is by using depth-first search.

The idea is we pick a direction, say left, and keep following pointers as far down left as we can go until we reach null. Once we reach null, we backtrack to the parent node and then go right. We keep doing this until we have visited every node in the tree. This is the essence of depth-first search. As the name implies, we go as deep as possible before we backtrack.

There are three ways to traverse a tree using depth-first search:
1. Inorder
2. Preorder
3. Postorder

Depth first search is best implemented using recursion, although it is possible to implement it iteratively using a stack
```
            (4)
        /           \
       (3)          (6)
    /     \       /     \
   (2)          (5)     (7)
  /   \        /  \     /  \
```

## Inorder Traversal
An inorder traversal will recursively visit all the nodes in the left subtree, then visit the parent node, and finally visit all the nodes in the right subtree. In this case, "visit" could mean anything from printing the node to performing some operation on it
```py
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
```
The order in which these nodes will be visited is `[2, 3, 4, 5, 6, 7]`, which is sorted. It's important to note that an inorder traversal will only print the nodes in sorted order if the tree is a binary search tree. The reason the nodes will print in a sorted order is because of the BST property. Since we know all values to the left of a node are smaller, this means we won't hit our base case until we reach the left-most node which is also the smallest node. After visiting this, we will traverse up, visit the parent and then visit the right subtree.

## Preorder Traversal
Althernatively, preorder traversal will visit the parent node first, then visit the left subtree, and finally visit the right subtree.
```py
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
```
The nodes are visited in the following order `[4, 3, 2, 6, 5, 7]`

## Postorder Traversal
A postorder traversal will visit the left subtree, then the right subtree, and finally the parent node last.
```py
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
```
The order in which these nodes will be visited is `[2, 3, 5, 7, 6, 4]`

## Time and Space Complexity
### Time
We know that we have to visit every node in the tree, and if there are n nodes in the tree, the algorithm will run in O(n), regardless of the height of the tree. Another interesting point is that we could actually build a sorted array from the inorder traversal of a binary tree because the noes are visited in sorted order

### Space
The space complexity of the algorithm is O(h) where h is the height of the tree, which would be O(log n) for a balanced binary tree or O(n) for a skewed tree