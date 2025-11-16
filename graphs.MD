#  Graphs
- Definition: A graph $G$ is a non-linear data structure consisting of a set of vertices (or nodes) $V$ and a set of edges (or arcs) $E$ that connect pairs of vertices.

- Vertex (Node): Represents an entity or object in the real world (e.g., a city, a person, a webpage).Edge (Arc): Represents a relationship or connection between two vertices. 

- An edge $e$ is often expressed as an ordered or unordered pair of vertices $(u, v)$.

- Types of Graphs:
    - Undirected Graph: Edges have no direction; if $(u, v)$ is an edge, you can travel from $u$ to $v$ and from $v$ to $u$.
    - Directed Graph (Digraph): Edges have a specific direction, meaning the connection is one-way.

- Weighted vs. Unweighted:
    - Weighted Graph: Each edge has an associated numerical value called a weight or cost (e.g., distance, time, or cost).- Unweighted Graph: All edges are considered to have the same or no weight.

- Adjacency and Path:Adjacency: 
    - Two vertices are adjacent if they are connected by an edge.
    - Path: A sequence of edges that connects a sequence of distinct vertices.

- Representation: Graphs are typically represented in a computer using two main methods: the Adjacency Matrix or the Adjacency List.

# Algorithms for graphs

1. Breadth-First Search (BFS): An algorithm used for traversing (or searching) a graph data structure. It explores a graph layer by layer, visiting all the neighbors of a starting node first, before moving to the next level of neighbors. It is often used to find the shortest path in unweighted graphs.

2. Depth-First Search (DFS): Also a traversal algorithm that explores as far as possible along each branch before backtracking. It uses a stack (or recursion) and is useful for tasks like topological sorting, finding connected components, and cycle detection.

3. Dijkstra's Algorithm: A famous shortest path algorithm that finds the shortest paths from a single starting vertex to all other vertices in a weighted graph with non-negative edge weights. It is widely used in network routing.

4. Bellman-Ford Algorithm: Another shortest path algorithm, similar to Dijkstra's, but capable of handling graphs that contain negative edge weights. It can also detect if a graph has a negative-weight cycle.

5. Kruskal's Algorithm: A greedy algorithm used to find the Minimum Spanning Tree (MST) for a connected, weighted, undirected graph. An MST is a subset of the edges that connects all the vertices together, without any cycles, and with the minimum possible total edge weight.

6. Prim's Algorithm: An alternative greedy algorithm, also used to find the Minimum Spanning Tree (MST). Unlike Kruskal's, which builds a forest of trees, Prim's algorithm builds a single tree by continually adding the cheapest edge from a vertex already in the tree to one not yet in the tree.

7. Floyd-Warshall Algorithm: An algorithm used to find the shortest paths between all pairs of vertices in a weighted graph. It is an example of a dynamic programming approach.

```python
my_graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}
"""
typical dfs search - iterative
"""
def dfs(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)
"""
typical dfs search - recursive
"""
def dfs_recursive(graph, source):
    print(source)
    for neighbor in graph[source]:
        dfs_recursive(graph, neighbor)

"""
typical bfs search - iterative
"""
from collections import deque
def bfs_iterative(graph, source):
    queue = deque([source])

    while queue:
        current = queue.popleft()
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)
"""
find a path in a graph between 2 nodes
for undirected graph w/o cycles
dfs - recursive
"""
def has_path_dfs(graph, src, dst):
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True
    
    return False
"""
find a path dfs recursive for graphs that could have cycles.
"""
def has_path_dfs_detect_cycle(graph, src, dst, visited):
    if src == dst:
        return True
    
    if src in visited:
        return False
    
    visited.add(src)
    
    for neighbor in graph[src]:
        if has_path_dfs_detect_cycle(graph, neighbor, dst, visited):
            return True
    
    return False
"""
find a path in a graph between 2 nodes
for undirected graph w/o cycles
bfs - iterative
"""
from collections import deque
def has_path_bfs(graph, src, dst):
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    return False

# build directed graph from list of edges
edges = [
    ("i", "j"),
    ("k", "i"),
    ("m", "k"),
    ("k", "l"),
    ("o", "n")
]

def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge 
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

"""
connected components
"""
connected_count = {
    0: [8, 1, 5], 
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True

def connect_component_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1
    return count

"""
check for largest component in a graph
"""
all_components = {
    0: [8, 1, 5], 
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

def explore_size(graph, node, visited):
    if node in visited:
        return 0
    
    visited.add(node)
    size = 1
    for neighbor in graph[node]:
        size += explore_size(graph, neighbor, visited)

    return size

def largest_component(graph):
    longest = 0
    visited = set()
    for node in graph:
        size = explore_size(graph, node, visited)
        if size > longest:
            longest = size
    return longest


"""
shortest path between 2 nodes

"""
edges = [
    ["w", "x"],
    ["x", "y"],
    ["z", "y"],
    ["z", "v"],
    ["w", "v"]
]

def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge 
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def shortest_path(edges, node_a, node_b):

    graph = build_graph(edges)
    visited = set([node_a])
    queue = deque([(node_a, 0)])

    while queue:
        node, distance = queue.popleft()
        if node == node_b:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1


"""
Count island in a matrix,
land vs water
"""
grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]

def explore(grid, r, c, visited):
    row_inbound = 0 <= r and r < len(grid)
    col_inbound = 0 <= c and c < len(grid[0])
    if not row_inbound or not col_inbound:
        return False

    if grid[r][c] == "W":
        return False

    position = str(r) + "," + str(c)

    if position in visited:
        return False
    
    visited.add(position)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True



def island_count(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                print(r, c)
                count += 1
    
    return count


"""
Count the minimum number of island
"""
grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]

def explore_size(grid, r, c, visited):
    row_inbound = 0 <= r and r < len(grid)
    col_inbound = 0 <= c and c < len(grid[0])
    if not row_inbound or not col_inbound:
        return 0

    if grid[r][c] == "W":
        return 0

    position = str(r) + "," + str(c)

    if position in visited:
        return 0
    
    visited.add(position)
    size = 1
    size += explore_size(grid, r - 1, c, visited)
    size += explore_size(grid, r + 1, c, visited)
    size += explore_size(grid, r, c - 1, visited)
    size += explore_size(grid, r, c + 1, visited)

    return size

def minimum_island(grid):
    visited = set()
    min_count = float("inf")
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            current_size = explore_size(grid, r, c, visited)
            if current_size > 0 and current_size < min_count:
                min_count = current_size
    return min_count
```