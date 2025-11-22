# Binary Search

```python
# standard binary search algorithm
def binary_search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = left + ((right - left ) // 2)

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


## binary search on conditions for
## array of all false follow by all true
## will find the left most true
def binary_search_condition(arr):

    n = len(arr)
    left = 0
    right = n - 1

    while left < right:
        mid = left + ((right - left) // 2)

        if arr[mid]: 
            right = mid
        else:
            left = mid + 1
        
    return left
```

# Binary Search Tree
- has a left and right node
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
```
- pre_order traversal: node -> left -> right
```python
# recursive solution
def pre_order(node):
    if not node:
        return
    print(node) # process node in some way
    pre_order(node.left)
    pre_order(node.right)

# iterative solution
def pre_order(node):
    stack = [node]
    while stack:
        node = stack.pop()
        print(node) # process node in some way
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

- in_order traversal: left -> node -> right
```python
# recursive solution
def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node) # process node in some way
    in_order(node.right)
```
- post_order traversal: left -> right -> node
```python
# recursive solution
def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node) # process node in some way

# iterative solution aka level_order/breadth_first_search
def post_order(node):
    from collections import deque
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        print(node) # process node in some way
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
- Search in BST
```python
# recusive search for a regular binary tree, children does not
# necessary have any order to it. Just a node with 2 children.
def search_binary_tree(node, target):
    if not node:
        return False # could return val, true/false or anything else
    if node.val == target:
        return True

    return search_binary_tree(node.left, target) or search_binary_tree(node.right, target)


def search_bst(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    elif target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)

```

