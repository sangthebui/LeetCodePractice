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

```