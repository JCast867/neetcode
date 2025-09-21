# Breadth First Search
In depth-first search, we prioritized depth. For breath-first search (BFS), we prioritize breadth, meaning we focus on visiting all the nodes on one level before moving on to the next level. BFS is also known as level-order traversal when referring to trees, since we visit the nodes level by level

## Implementation
Generally, breadth-first search is implemented iteratively. Since we want to visit all the nodes on one level before moving to the next, we will need a data structure that allows us to do this. A **queue** data structure, more specifically, a deque, allows us to remove elements both from the head and the tail in O(1) time. For BFS, we will append elements to the tail and remove elements from the head as we go through each level of the tree from left to right
```py
def bfs(root):
    queue = deque()

    if root:
        queue.append(root)
    
    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1
```
1. Initially, we append the root node to our queue
2. We then enter a while loop that runs as long as our queue is not empty
3. We print the level we're currently on
4. We loop through the queue and remove nodes in the current level
5. If the node has children, we append them to the queue from left to right
6. After the current level is done, we increment the level by 1
7. Our queue becomes empty once we have visited all of the nodes and the outer while loop will terminate

## Time and Space Complexity
### Time
The time complexity of BFS is O(n) where n is the number of nodes in the tree. This is because we visit every node exactly once

### Space
The space complexity of BFS is O(n) where n is the number of nodes in the tree. This is because we ill store an entire level of the tree in the queue at a time. In the worst case, the last level may be roughlt half the size of the tree, so the space complexity is O(n)