# Stack Vs. Queue
- Stack for Depth-First-Search (DFS)
    - Pre-order traversal (Root, Left, Right)
    - Reverse pre-order traversal (Root, Right, Left)
    - In-order traversal (Left, Root, Right)
    - Post-order traversal (Left, Right, Root)
- Queue for Breadth-First-Search (BFS)
    - Level-order traversal (This is another name for BFS)

## Monotonic Stack
- Used to keep track of the next greater element, next smaller element, previous greater element, previous smaller element, First element to the left/right that satisfies some ordering condition
- maintained sorted order on the stack - either increasing or decreasing
order. Keeps algorithm in O(n) for problems that would be O(n^2) otherwise.



```python
input = [2, 1, 2, 4, 3]
# expected answer is [4, 2, 4, -1, -1]
stack = []
result = [-1] * len(input)

for i in range(len(input) - 1, -1, -1):
    current = input[i]
    
    while stack and stack[-1] <= current:
        stack.pop()
    if stack:
        result[i] = stack[-1]

    stack.append(current)


```