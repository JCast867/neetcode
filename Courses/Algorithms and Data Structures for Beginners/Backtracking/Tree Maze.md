# Backtracking
Backtracking is an algorithm with a lot of overlap with DFS. It operates on a brute-force approach which is to try all possible solutions and backtrack when we hit a dead-end. Imagine we're trapped in a maze and we are trying to find our way out. We can try all possible paths until we find the correct one. If we hit a dead-end, we backtrack and try another path. This is the essence of backtracking

## Motivation with Example
Given a binary tree, we want to determine if there exists a path from the root to a leaf node without having a value of `0` in the path. If such a path exists, we return `true`, otherwise we return `false`

The first thing that comes to mind is using depth-frist search. Our constraint is that we cannot have a node with value `o` in our path. We also know that if the tree is empty, then there cannot exist a valid path either. Finally, if we reach a leaf node, we can return `true` since it means there is a path that exists from root to leaf

If there is a solution, it will either be in the left-subtree or the right-subtree
1. We can arbitrarily choose to explore the left-subtree first
2. If the left-subtree return `true`, we can return `true` as well
3. If the left-subtree return `false`, we can explore the right-subtree
4. If the right-subtree return `true`, we can return `true` as well
5. If both the left and right subtrees return `false`, we can return `false` as well

```py
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def canReachLeaf(root):
    if not root or root.val == 0:
        return False

    if not root.left and not root.right:
        return True
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    return False
```
## Building the Path
Let's take a look at a slight variation of the question where instead of just returning `true` or `false`, we also build the path if it exists. The path should contain the values of the root to the leaf path in the order they are visited
```
            (4)
        /         \
tree = (0)         (1)
    /    \        /     \
         (7)    (3)     (2)
       /    \   /   \    /  \
                    (0)
```

In this problem, we can pass a parameter `path`, which is a list to store all the nodes that are in the valid path. So given the tree `tree`, we first add the root node to our list. Since there is only one valid path, it will either be in the left-subtree or the right-subtree
1. The left-subtree is invalid because `4`'s left child is `0`, thus we return false and now recursively check the right-subtree
2. Going to the right, `1` is valid, so we add it to our list
3. Now we check `3`, which is valid, so it gets added to our list
4. `3`'s left child is null so we return false
5. Checking `3`'s right child, we again hit the base case
6. Now we must remove `3` from our stack because if there existed a valid path, we would have returned true already
7. We go back up to `3`'s parent, which is `1`, and check its right subtree
8. We add `2` to our list. We then explore `2` but 2 is a lead node, which makes the recursive call return true, after which the function returns true
9. Our valid path is `[4, 1, 2]`

```py
def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)

    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False
```

## Time and Space Complexity
### Time
Given that the tree has n nodes, the time complexity will be O(n) because in the worst case, we may need to visit all the nodes in the tree

### Space
The space complexity is O(h) where h is the height of the tree. This is because we are using recursion and the maximum depth of the recursion is the height of the tree. We are also storing the nodes along the path in the `path` list, which will have a maximum of O(h) elements at any given time
