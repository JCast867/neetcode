# Recursion (Two Branch)
A more common case of recursion is multi-branch recursion. The Fibonacci sequence is a set of numbers that start with 0 and 1, and each subsequent number is the sum of the two preceding numbers. The sequence starts 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,... Generally, the formula to calculate the nth fibonacci number is to sum the previous fibonacci numbers, i.e. the (n - 1)th and (n - 2)th fibonacci numbers. For formally, we say that:
1. F(0) = 0 and F(1) = 1
2. F(n) = F(n - 1) + F(n - 2)
Part 1 is the base case and part 2 is the recursive case. 
```py
# recursive implementation to calculate the n-th fibonacci number
def fibonacci(n):
    # base case
    if n <= 1:
        return n
    
    # recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)
```
## Steps for Code
We have our base case, we know the function calls itself in the last return statement, and we know that at some point when the base case is reached, we will have to travel back "up" to calculate the ultimate answer.
1. To calculate `fibonacci(5)`, we get `fibonacci(4) + fibonacci(3)`
2. Now, both of these will execute within their own function calls. Looking at
3. `fibonacci(4)` will call `fibonacci(3) + fibonacci(2)` and so on, until `n` hits `1` or `0`
4. After that, it will return the result and keep going back up all the way until `fibonacci(4) which will give us an answer of 3
5. Now, we have the answer to `fibonacci(4)` and do the same for `fibonacci(3)` which results in 2
6. Add the two together, and the 5th fibonacci number is 5

## Time and Space Complexity
Evaulating the time complexity for this is a little bit more tricky. On the 1st level, there is 1 node, on the 2nd level, there are 2, then 4, after which we can see a pattern. Each level has the potential to hold 2x the nodes of the previous level. Therefore, a reasonable upperbound for the total number of nodes in the tree is 1 + 2 + 4 + 8 + ... + 2^n. This is a geometric series. We know the last term is the dominating term, and the sum of the series is roughly 2^n+1 - 1. This means that the total number of nodes in the tree is O(2^n). Each node itself is a function call and simply calculates the sum of two values, thus the time complexity of the function is O(2^n)