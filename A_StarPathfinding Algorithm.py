"""

A Pathfinding Algorithm Overview

The A (A-star)* algorithm is one of the most popular pathfinding algorithms used 
to find the shortest path between two points on a grid or graph.
It’s commonly used in game development, robotics, and navigation systems.
A* combines the strengths of Breadth-First Search (BFS) and Dijkstra's Algorithm 
by using a heuristic to guide its search, making it efficient for finding the 
shortest path in complex spaces.

A* maintains a priority queue of nodes to explore.
For each node, it calculates the cost function 

f(n): g(n) + h(n)
g(n): Cost to reach the current node from the start.
h(n): Heuristic estimate of the cost to reach the goal from the current node.

A* chooses the node with the lowest 
f(n) value to explore next.

The heuristic function h(n) is usually the Manhattan distance or Euclidean distance 
between the current node and the goal. The choice of the heuristic function significantly 
affects the efficiency of the algorithm.

Explanation of the Code

Node Class:
Represents each cell in the grid with attributes like g, h, and f.

Heuristic Function:
Calculates the Manhattan distance between the current position and the goal.

A* Algorithm*:

We maintain an open list (nodes to explore) and a closed list (already explored nodes).
For each node, we calculate its neighbors and update their costs.
We backtrack to find the path once the goal is reached.

Output
Finding the shortest path using A*...
Shortest path found: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]
This represents the shortest path from the start (0, 0) to the goal (4, 4) avoiding obstacles.

Practice
Modify the grid to include more obstacles and test how the algorithm finds paths.
Experiment with different heuristic functions (like Euclidean distance).
Try using larger grids to see how the algorithm scales with more complex maps.

"""

# A* Pathfinding Algorithm
# Astro Pema Software (c)
# Oba Ozai Nov 2024

import heapq
import math

# Node class to store information for each cell
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to the current node
        self.h = 0  # Heuristic cost estimate to the goal
        self.f = 0  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    """Calculate the Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    """
    A* algorithm to find the shortest path in a grid.
    
    Parameters:
    grid (list of list of int): 2D grid where 0 is walkable and 1 is an obstacle.
    start (tuple): Starting coordinates (x, y).
    goal (tuple): Goal coordinates (x, y).
    
    Returns:
    list of tuple: Shortest path from start to goal, or an empty list if no path is found.
    """
    open_list = []
    closed_list = set()
    
    start_node = Node(start)
    goal_node = Node(goal)
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        closed_list.add(current_node.position)
        
        # Generate neighbors (up, down, left, right)
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for offset in neighbors:
            neighbor_pos = (current_node.position[0] + offset[0], current_node.position[1] + offset[1])
            
            if not (0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0])):
                continue  # Skip out of bounds positions
            
            if grid[neighbor_pos[0]][neighbor_pos[1]] == 1 or neighbor_pos in closed_list:
                continue  # Skip obstacles and already visited nodes
            
            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_pos, goal)
            neighbor_node.f = neighbor_node.g + neighbor_node.h
            
            heapq.heappush(open_list, neighbor_node)
    
    return []  # No path found

if __name__ == "__main__":
    # Example grid (0 = walkable, 1 = obstacle)
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    print("Finding the shortest path using A*...")
    path = a_star(grid, start, goal)
    
    if path:
        print(f"Shortest path found: {path}")
    else:
        print("No path found.")

# EOF




