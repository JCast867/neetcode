# Recursion (One Branch)
Recursion is when a function calls itself, usually with a different input. This is known as a **recursive function**. Recursive functions can be thought of as functions that breaks down a problem into smaller sub-problems and solves them in reverse order. It's usually possible to convert a recursive function into an iterative one, and vice versa. The recursive function has two parts. The base case and the recursive case. 

## About
If we want to compute n! (n-factorial), we can use recursion. The formula for n! is n * (n - 1) * (n - 2) * ... * 1. For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.
1. Notice the 5! can be broken down into 5 * 4!
2. 4! can be broken down into 4 * 3!, and so on. This is the recursive case
3. The base case is when n = 0 or n = 1. The result of 0! and 1! is 1

```py
# recursive implementation of n!
def factorial(n):
    # base case
    if n <= 1:
        return 1
    
    # recursive case
    return n * factorial(n - 1)
```
We have two parts. The **base case** and the **recursive case**. When the code reaches the last line with the initial input of 5, we get: `5 * factorial(4)`, which starts executing the function again but with input 4. So we get `4 * factorial(3)` and then `3 * factorial(2)` and lastly `2 * factorial(1)` after which the base case is reached. But what happends when the base case is reached? When the function is called with 1 as the input, 1 is returned. And now it can be multiplied by 2, which will result in 2, which is the answer to 2!. We have only solved the first sub-problem so far. Now we compute `3 * factorial(2)`, which results in 6, then `4 * factorial(3)`, which is 24, and finally `5 * factorial(4)` which is 120. The final answer to 5!. The most important part is that when we trigger the base case, we move back "up" the recursion tree because now we have to "piece" together the answers to our sub-problems to get the final solution. The complicated part about this is that you have to think about the problem in reverse order.

## Time and Space Complexity
Time: O(n)
* In total, n calls are being made to `factorial`, where each function call is O(1), making the total time complexity O(n)


Space: O(n)
* While we're not using any data structures, the recursion operates off an implicit stack, known as the function call stack. That's how we are able to return from one function call to the previous one. Since there are n recursive calls, there will be n function calls placed on the stack, which results in O(n) space.