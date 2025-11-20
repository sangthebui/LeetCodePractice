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

# Python Stacks
## use python list
### append(element) 
    - Adds a single element to the end of the list.
### clear() 
    - Removes all elements from the list, making it empty.
### copy() 
    - Returns a shallow copy of the list.
### count(value) 
    - Returns the number of elements with the specified value.
### extend(iterable) 
    - Adds elements of an iterable to the end of the list.
### index(value, start=0, end=None) 
    - Returns the index of the first element with the specified value.
### insert(index, element) 
    - Adds an element at the specified position.
### pop(index=None) 
    - Removes the element at the specified position.
### remove(value) 
    - Removes the first item with the specified value.
### reverse() 
    - Reverses the order of the list.
### sort(key=None, reverse=False) 
    - Sorts the list.

```python
# Initial list for examples
fruits = ['apple', 'banana', 'cherry', 'date', 'apple']
print(f"Initial List: {fruits}\n")

# 1. append(element)
fruits.append('elderberry')
print(f"1. append: {fruits}")
# Output: ['apple', 'banana', 'cherry', 'date', 'apple', 'elderberry']

# 2. extend(iterable)
citrus = ['lemon', 'lime']
fruits.extend(citrus)
print(f"2. extend: {fruits}")
# Output: ['apple', 'banana', 'cherry', 'date', 'apple', 'elderberry', 'lemon', 'lime']

# 3. insert(index, element)
fruits.insert(1, 'avocado')
print(f"3. insert: {fruits}")
# Output: ['apple', 'avocado', 'banana', 'cherry', 'date', 'apple', 'elderberry', 'lemon', 'lime']

# 4. remove(value)
# Removes the first occurrence of 'apple'
fruits.remove('apple')
print(f"4. remove: {fruits}")
# Output: ['avocado', 'banana', 'cherry', 'date', 'apple', 'elderberry', 'lemon', 'lime']

# 5. pop(index=-1)
# Pop the last item (default index)
popped_item = fruits.pop()
print(f"5. pop (last item): {popped_item}")
print(f"   List after pop: {fruits}")
# Output: pop (last item): lime
# Output: List after pop: ['avocado', 'banana', 'cherry', 'date', 'apple', 'elderberry', 'lemon']

# Pop a specific index (e.g., index 0: 'avocado')
popped_avocado = fruits.pop(0)
print(f"   Pop index 0: {popped_avocado}")
print(f"   List after pop(0): {fruits}")
# Output: Pop index 0: avocado
# Output: List after pop(0): ['banana', 'cherry', 'date', 'apple', 'elderberry', 'lemon']

# 6. index(value, start, end)
index_of_cherry = fruits.index('cherry')
print(f"6. index('cherry'): {index_of_cherry}")
# Output: index('cherry'): 1

# 7. count(value)
apple_count = fruits.count('apple')
print(f"7. count('apple'): {apple_count}")
# Output: count('apple'): 1

# 8. sort(key=None, reverse=False)
fruits.sort()
print(f"8. sort (ascending): {fruits}")
# Output: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'lemon']

fruits.sort(reverse=True)
print(f"   sort (descending): {fruits}")
# Output: ['lemon', 'elderberry', 'date', 'cherry', 'banana', 'apple']

# 9. reverse()
fruits.reverse()
print(f"9. reverse: {fruits}")
# Output: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'lemon'] (back to original 'sorted ascending' order)

# 10. copy()
fruits_copy = fruits.copy()
fruits_copy.append('mango') # Modify the copy
print(f"10. copy: {fruits_copy} (Copy modified)")
print(f"    Original List remains: {fruits}")
# Output: copy: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'lemon', 'mango']
# Output: Original List remains: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'lemon']

# 11. clear()
fruits.clear()
print(f"11. clear: {fruits}")
# Output: clear: []

```


# Python Queues
## use collections deque
### append(element) 
    - Adds a single element to the right end of the queue.
### appendleft(element) 
    - Adds a single element to the left end of the queue.
### clear() 
    - Removes all elements from the queue, making it empty.
### copy() 
    - Returns a shallow copy of the queue.
### count(value) 
    - Returns the number of elements with the specified value.
### extend(iterable)
    - Adds elements of an iterable to the right end of the queue.
### extendleft(iterable)
    - Adds elements of an iterable to the left end of the queue.
### index(value, [start, [end]])
    - Returns the position of the first occurrence of value within the deque, searching between start and end if provided. Raises ValueError if value is not found.
### insert(index, element)
    -  Inserts element into the deque at position index
### maxlen() 
    - Returns the maximum size of the queue.
### pop() 
    - Removes and returns the element from the right end of the queue.
### popleft() 
    - Removes and returns the element from the left end of the queue.
### remove(value) 
    - Removes the first occurrence of the specified value.
### reverse() 
    - Reverses the order of the queue.
### rotate(n=1)
    - Rotates the elements in the queue.


```python
from collections import deque

# 1. Initialization
dq = deque([10, 20, 30], maxlen=10) # Create a deque with initial elements and a max length
print(f"Initial Deque: {dq}")
# Initial Deque: deque([10, 20, 30], maxlen=10)

# 2. append(x): Add to the right
dq.append(40)
print(f"After append(40): {dq}")
# After append(40): deque([10, 20, 30, 40], maxlen=10)

# 3. appendleft(x): Add to the left
dq.appendleft(5)
print(f"After appendleft(5): {dq}")
# After appendleft(5): deque([5, 10, 20, 30, 40], maxlen=10)

# 4. extend(iterable): Extend from the right
dq.extend([50, 60])
print(f"After extend([50, 60]): {dq}")
# After extend([50, 60]): deque([5, 10, 20, 30, 40, 50, 60], maxlen=10)

# 5. extendleft(iterable): Extend from the left (elements added in reverse order)
dq.extendleft([0, 2])
print(f"After extendleft([0, 2]): {dq}")
# After extendleft([0, 2]): deque([2, 0, 5, 10, 20, 30, 40, 50, 60], maxlen=10)

# 6. pop(): Remove and return from the right
right_item = dq.pop()
print(f"Popped right item: {right_item}, Deque after pop(): {dq}")
# Popped right item: 60, Deque after pop(): deque([2, 0, 5, 10, 20, 30, 40, 50], maxlen=10)


# 7. popleft(): Remove and return from the left
left_item = dq.popleft()
print(f"Popped left item: {left_item}, Deque after popleft(): {dq}")
# # 7. popleft(): Remove and return from the left
left_item = dq.popleft()
# Popped left item: 2, Deque after popleft(): deque([0, 5, 10, 20, 30, 40, 50], maxlen=10)


# 8. insert(i, x): Insert at an index (less efficient, use append/pop when possible)
# Note: Deques aren't optimized for middle inserts/deletes, but the method exists.
dq.insert(2, 25) 
print(f"After insert(2, 25): {dq}")
# After insert(2, 25): deque([0, 5, 25, 10, 20, 30, 40, 50], maxlen=10)


# 9. remove(value): Remove the first occurrence of a value
try:
    dq.remove(25)
    print(f"After remove(25): {dq}")
except ValueError:
    print("Value not found for remove operation.")
# After remove(25): deque([0, 5, 10, 20, 30, 40, 50], maxlen=10)



# 10. count(value): Count occurrences
dq.extend([10, 10]) # Add some duplicate values
count_of_10 = dq.count(10)
print(f"After adding duplicates, count of 10 is: {count_of_10}")
#  After adding duplicates, count of 10 is: 3



# 11. index(value, [start, [stop]]): Find index of first occurrence
try:
    index_of_30 = dq.index(30)
    print(f"Index of 30 is: {index_of_30}")
except ValueError:
    print("Value not found for index operation.")
# Index of 30 is: 5

# 12. reverse(): Reverse elements in-place
dq.reverse()
print(f"After reverse(): {dq}")
# After reverse(): deque([10, 10, 50, 40, 30, 20, 10, 5, 0], maxlen=10)


# 13. rotate(n): Rotate the deque
dq.rotate(2) # Positive n rotates right
print(f"After rotate(2) (right): {dq}")
dq.rotate(-2) # Negative n rotates left
print(f"After rotate(-2) (left): {dq}")
# After rotate(2) (right): deque([5, 0, 10, 10, 50, 40, 30, 20, 10], maxlen=10)
# After rotate(-2) (left): deque([10, 10, 50, 40, 30, 20, 10, 5, 0], maxlen=10)


# 14. clear(): Remove all elements
dq.clear()
print(f"After clear(): {dq}")
# After clear(): deque([], maxlen=10)

```


