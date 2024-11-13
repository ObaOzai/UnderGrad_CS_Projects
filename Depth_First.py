"""

Depth-First Search (DFS) Overview
DFS is a graph traversal algorithm used to explore nodes and edges of a graph systematically.
It explores as far down one branch as possible before backtracking.
DFS can be implemented using either recursion (implicitly using the call stack) or iteration (using an explicit stack).
It’s useful for tasks like finding connected components, detecting cycles, topological sorting, and solving puzzles like mazes.

Time Complexity: O(V+E), 
where 
V is the number of vertices and 
E is the number of edges.

Explanation of the Code
Graph Representation:
The graph is represented as a dictionary where each key is a node, and the value is a list of its neighbors.
Example:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

Iterative DFS (Stack):
We use a stack to keep track of nodes to visit.
Nodes are visited in depth-first order by popping from the stack.
Recursive DFS:
The function uses recursion to visit each node.
The visited set ensures that each node is only visited once.
Output
For both versions (iterative and recursive), 

DFS traversal starting from A:
['A', 'B', 'D', 'E', 'F', 'C']

Recursive DFS traversal:
A B D E F C 

Recurcive version:

# Depth-First Search (Recursive) Algorithm
# Astro Pema Software (c)
# Oba Ozai Nov 2024


recursive

def dfs_recursive(graph, node, visited=None):
    """
    Perform Depth-First Search on a graph using recursion.
    
    Parameters:
    graph (dict): Adjacency list representation of the graph.
    node (str): The current node being visited.
    visited (set): A set of visited nodes.
    
    Returns:
    list: A list of nodes visited in DFS order.
    """
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end=' ')  # Print the node as it's visited

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Sample graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Testing the recursive DFS function
if __name__ == "__main__":
    start_node = 'A'
    print("\nRecursive DFS traversal:")
    dfs_recursive(graph, start_node)

# EOF

"""

# Depth-First Search (Iterative) Algorithm
# Astro Pema Software (c)
# Oba Ozai Nov 2024

def dfs_iterative(graph, start):
    """
    Perform Depth-First Search on a graph using a stack.
    
    Parameters:
    graph (dict): Adjacency list representation of the graph.
    start (str): The starting node for DFS.
    
    Returns:
    list: A list of nodes visited in DFS order.
    """
    visited = set()  # To keep track of visited nodes
    stack = [start]  # Stack to manage the nodes to visit
    result = []

    while stack:
        # Pop a node from the stack
        node = stack.pop()

        if node not in visited:
            # Mark the node as visited and add it to the result
            visited.add(node)
            result.append(node)

            # Add all unvisited neighbors to the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
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

# Testing the iterative DFS function
if __name__ == "__main__":
    start_node = 'A'
    print(f"DFS traversal starting from {start_node}:")
    print(dfs_iterative(graph, start_node))

# EOF




