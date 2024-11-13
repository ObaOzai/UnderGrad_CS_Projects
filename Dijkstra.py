"""
Dijkstra's Algorithm Overview
Dijkstra's Algorithm is used to find the shortest path from a source vertex to all other vertices in a graph with non-negative edge weights.
It's widely used in network routing, mapping applications (like GPS navigation), and other optimization problems.
The algorithm uses a priority queue (usually implemented with a min-heap) to always expand the shortest path first.
Time Complexity: 

O((V+E)logV)), where 
V is the number of vertices and 
E is the number of edges.

Explanation of the Code
Graph Representation:
The graph is represented as a dictionary of lists of tuples, where each key is a vertex, 
and the value is a list of tuples representing neighbors and their weights.

Example:

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

Priority Queue:
The algorithm uses a priority queue to keep track of the shortest distances discovered so far.
The heapq library is used to implement the priority queue efficiently.

Distance Updates:
The distances dictionary keeps track of the shortest known distance to each vertex.
If a shorter path to a vertex is found, the distance is updated, and the vertex is added to the priority queue.

Output:
The function returns a dictionary with the shortest distance from the starting vertex to each vertex in the graph.

Output

Shortest paths from A:
Distance to A: 0
Distance to B: 1
Distance to C: 3
Distance to D: 4

"""

# Dijkstra's Algorithm
# Astro Pema Software (c)
# Oba Ozai Nov 2024

import heapq

def dijkstra(graph, start):
    """
    Function to find the shortest path from a starting vertex to all other vertices using Dijkstra's Algorithm.
    
    Parameters:
    graph (dict): A dictionary representing the graph where keys are vertices and values are lists of tuples (neighbor, weight).
    start (str): The starting vertex.
    
    Returns:
    dict: A dictionary of shortest distances from the starting vertex to each other vertex.
    """
    # Initialize distances with infinity for all vertices except the start vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Priority queue to store (distance, vertex)
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Extract the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Skip if a shorter path to the current vertex has already been found
        if current_distance > distances[current_vertex]:
            continue
        
        # Check neighbors of the current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found, update its distance and add to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Testing Dijkstra's Algorithm
if __name__ == "__main__":
    # Define a sample graph as an adjacency list
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    
    start_vertex = 'A'
    print(f"Shortest paths from {start_vertex}:")
    shortest_paths = dijkstra(graph, start_vertex)
    
    # Print the shortest distances
    for vertex, distance in shortest_paths.items():
        print(f"Distance to {vertex}: {distance}")

# EOF
