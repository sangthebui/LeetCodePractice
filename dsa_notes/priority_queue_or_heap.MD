# Priority Queue or Heap
- Structure: A heap is typically implemented as a complete binary tree, meaning all levels are fully filled, except possibly the last level, which is filled from left to right. This structure allows efficient array representation.

- Heap Property: Heaps maintain a specific ordering among parent and child nodes. There are two main types:
    - Max-Heap: The value of a parent node is always greater than or equal to the values of its children. The largest element is always at the root.
    - Min-Heap: The value of a parent node is always less than or equal to the values of its children. The smallest element is always at the root.

- Implementation: Due to its complete binary tree nature, a heap is most often implemented using a simple array or list, where the relationships between parent and child nodes can be calculated using array indices.

- Peak Element Access: The element with the highest (Max-Heap) or lowest (Min-Heap) priority is always at the root of the tree (index 0 in an array implementation), allowing for $O(1)$ access (constant time).

- Insertion (Push) Time Complexity: Inserting a new element into a heap takes $O(\log n)$ time, where $n$ is the number of elements. This involves placing the new element at the end and then performing a "heapify-up" or "sift-up" operation to restore the heap property.Deletion (Pop/Extract) Time Complexity: 

- Deleting the root (the max/min element) also takes $O(\log n)$ time. This involves replacing the root with the last element, removing the last element, and then performing a "heapify-down" or "sift-down" operation to restore the heap property.

- Primary Application: Heaps are the fundamental data structure used to efficiently implement a Priority Queue, and they are also the basis for the Heapsort sorting algorithm.

```python
import heapq

class MinHeap:
    def __init__(self):
        # The heap is stored as a simple list
        # no need to call headq.heapify because list is empty
        self.heap = []

    def push(self, item):
        """Adds an item to the heap."""
        # heapq.heappush maintains the min-heap property
        heapq.heappush(self.heap, item)

    def pop(self):
        """Removes and returns the smallest item from the heap."""
        # heapq.heappop removes and returns the smallest item (root)
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def peek(self):
        """Returns the smallest item without removing it."""
        # The smallest item is always at index 0
        if self.heap:
            return self.heap[0]
        return None

    def is_empty(self):
        """Checks if the heap is empty."""
        return len(self.heap) == 0


class MaxHeap:
    def __init__(self):
        # The heap is stored as a simple list
        self.heap = []

    def push(self, item):
        """Adds an item to the heap as its negative value."""
        # Store the negative value to simulate max-heap behavior
        heapq.heappush(self.heap, -item)

    def pop(self):
        """Removes and returns the largest item (by negating the result)."""
        if self.heap:
            # Negate the popped value to get the original maximum
            return -heapq.heappop(self.heap)
        return None

    def peek(self):
        """Returns the largest item without removing it."""
        if self.heap:
            # Negate the value at index 0 to get the original maximum
            return -self.heap[0]
        return None

    def is_empty(self):
        """Checks if the heap is empty."""
        return len(self.heap) == 0
```