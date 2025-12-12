# For easy questions,

- usually it consists of 1 concept.

# For medium questions,

- usually it consists of at least 2 concepts.

# For hard questions,

- usually there are multiple ways of solving the question,
- but there is always one solution that is better than the rest
- the question that is asking usually has another view to it.

# Tools at your disposals

- Nothing is off the table

## Regular arrays or strings

- for simple problems, not only easy, but the problem does not neeed a more complex data structure

## Stacks, could be multiples

- Regular stacks
- Monotonic stacks, both ways, could be multiples stacks also

## Queues, could be multiples

- Regular queues, could be mutliples

### Heaps, Could be multiples

- Specialized queues that is ordered
- Priority queues or heap
- Indexed priority queues
- Fibonacci priority queues

## Hashmap or Hashsets or Hashtables

- Counters, for counting frequency
-

## Trees

- most common is binary trees
- binary search trees
- sometimes need different tree traversal algo for different questions.
- BFS or DFS
- detect cycles, paths, heights, widths, sum, etc...

## Graphs

- for medium to hard questions
-

## Tries or Prefix Trees

## Algorithms

- prefix sum
- two pointers
- sliding windows
- modular arithmetic - for dealing with large numbers
- dynamic programming
- greedy
- backtracking
- bit manipulations
- discrete math knowledge
- searching
- sorting

## Uncommon data structures (variations of data structures)

- Skip lists
-

## LeetCode python modules

- **almost all modules from the Python standard library.**
- **External, third-party libraries (like Django or requests) are generally not available, except for certain exceptions like NumPy and Pandas in specific environments.**

- collections: Provides specialized container datatypes like deque (for O(1) append and pop from both ends, useful for BFS and queues), Counter (for counting hashable objects), and defaultdict.
- heapq: Offers an implementation of the heap queue algorithm (priority queue), with methods like heappush and heappop, which are crucial for problems involving priority queues or finding the smallest/largest elements efficiently.
- bisect: Functions for manipulating sorted lists using a binary search algorithm, useful for inserting items into a list while maintaining sorted order.
- itertools: Functions for creating efficient iterators, such as permutations and combinations, which are helpful for combinatorial problems.
- math: Provides access to common mathematical functions and constants, useful in many algorithm problems.
  functools: Contains higher-order functions like lru_cache for memoization (dynamic programming optimization).
- re: Support for regular expressions.
- sys: Provides access to some system-specific parameters and functions, such as increasing recursion depth (sys.setrecursionlimit).
- **sys.setrecursionlimit(10\*\*6)**

### From LeetCode official page for python3

- Most libraries are already imported automatically for your convenience, such as array, bisect, collections. If you need more libraries, you can import it yourself.

- For Map/TreeMap data structure, you may use sortedcontainers library.
- Python 3.11
