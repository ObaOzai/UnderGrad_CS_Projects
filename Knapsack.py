"""

Knapsack Problem Overview
The Knapsack Problem is a classic optimization problem where you have a set of items,
each with a weight and a value. Your goal is to maximize the total value without exceeding 
a given weight capacity. The 0/1 Knapsack Problem is the version where each item can either be 
included in the knapsack or excluded (can’t take fractional items).

Dynamic Programming is used to solve the problem efficiently by breaking it down into 
subproblems and using a table to store the solutions to these subproblems.

Time Complexity: 

O(nW), where n is the number of items and 
W is the maximum weight capacity of the knapsack.

Explanation of the Code
Table Initialization:
A 2D list dp is created to store the maximum value that can be achieved for each item and weight capacity.
dp[i][w] represents the maximum value that can be achieved using the first 
i items and a knapsack capacity of w.

Filling the Table:
We use a bottom-up approach to fill the table.
For each item and weight, we decide whether to include the item in the knapsack.
If the item's weight is less than or equal to the current capacity 
w, we have two choices:

Include the item and add its value to the solution of the remaining capacity.
or Exclude the item.

We take the maximum of these two options.
Result:
The bottom-right cell of the table dp[n][capacity] contains the maximum value that can be achieved with the given items and capacity.

Weights: [2, 3, 4, 5]
Values: [3, 4, 5, 6]
Maximum weight capacity: 5
Maximum value that can be achieved: 7

Try changing the weights, values, and capacity to experiment with different scenarios.
Test how the algorithm handles larger inputs to see the efficiency of dynamic programming.

"""

# Knapsack Problem using Dynamic Programming
# Astro Pema Software (c)
# Oba Ozai Nov 2024

def knapsack(weights, values, capacity):
    """
    Solve the 0/1 Knapsack Problem using Dynamic Programming.
    
    Parameters:
    weights (list): List of weights of the items.
    values (list): List of values of the items.
    capacity (int): Maximum weight capacity of the knapsack.
    
    Returns:
    int: The maximum value that can be achieved within the given capacity.
    """
    n = len(values)
    # Initialize a table to store the maximum value for each capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the table using a bottom-up approach
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Item can be included
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Item cannot be included
                dp[i][w] = dp[i - 1][w]

    # The bottom-right cell contains the maximum value for the given capacity
    return dp[n][capacity]

# Testing the Knapsack function
if __name__ == "__main__":
    # Sample items with weights and values
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    print("Weights:", weights)
    print("Values:", values)
    print("Maximum weight capacity:", capacity)
    
    max_value = knapsack(weights, values, capacity)
    print(f"Maximum value that can be achieved: {max_value}")

# EOF



