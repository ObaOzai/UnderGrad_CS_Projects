"""

Breadth-First Search (BFS) Overview

BFS is a graph traversal algorithm used to explore nodes level by level, starting from a given source node.
It explores all the neighbors of a node before moving on to the neighbors' neighbors.
BFS is particularly useful for finding the shortest path in unweighted graphs and for 
solving problems like finding connected components.


Time Complexity: 
O(V+E), where 
V is the number of vertices and 
E is the number of edges.

Explanation of the Code
Graph Representation:

The graph is represented as a dictionary (adjacency list).
Each key represents a node, and the value is a list of its neighbors.

Queue Initialization:
We use Python’s deque for efficient queue operations.
The queue is initialized with the start node.

Traversal:
Nodes are dequeued one by one.
Each dequeued node is marked as visited and added to the result list.
The neighbors of the current node are enqueued if they haven't been visited yet.

Output
BFS traversal starting from A:
['A', 'B', 'C', 'D', 'E', 'F']

"""

# Breadth-First Search (BFS) Algorithm
# Astro Pema Software (c)
# Oba Ozai Nov 2024

from collections import deque

def bfs(graph, start):
    """
    Perform Breadth-First Search on a graph using a queue.
    
    Parameters:
    graph (dict): Adjacency list representation of the graph.
    start (str): The starting node for BFS.
    
    Returns:
    list: A list of nodes visited in BFS order.
    """
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Queue to manage the nodes to visit
    result = []

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            result.append(node)

            # Enqueue all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

# Sample graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Testing the BFS function
if __name__ == "__main__":
    start_node = 'A'
    print(f"BFS traversal starting from {start_node}:")
    print(bfs(graph, start_node))

# EOF


