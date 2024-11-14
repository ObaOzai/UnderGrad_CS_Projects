"""

Simulated Annealing Overview

Simulated Annealing is an optimization algorithm inspired by the process of annealing in metallurgy,
where metals are slowly cooled to reduce defects.

The algorithm is used to find an approximate solution to optimization problems by exploring the 
solution space probabilistically.

It can escape local optima by allowing moves that increase the objective 
function’s value, especially in the early stages of the search.
Applications: Traveling salesman problem, scheduling, circuit design, 
machine learning model optimization.

Concept

Objective Function: Define the function you want to optimize (either maximize or minimize).
Temperature: A control parameter that starts high and gradually decreases. 
Higher temperatures allow more exploration, while lower temperatures focus on refinement.

Acceptance Probability:
If the new solution is better, accept it.
If it's worse, accept it with a probability based on the temperature:

P(accept)=e^ΔE/T

We’ll use Simulated Annealing to solve a simple optimization problem: finding the minimum of a mathematical function.

Objective Function

Let's optimize the function:

f(x)=x^2+4cos(2x) We want to find the value of x that minimizes this function.

Simulated Annealing Algorithm:

We initialize a random starting point initial_x and set the initial temperature.
At each iteration, we generate a new candidate solution by making a small change 
to the current solution.

If the new solution is better, we accept it. 

If it's worse, we accept it with a probability that decreases with the temperature.
The temperature decreases gradually with each iteration.

Measuring Performance:
We use time.time() to measure the time taken by the algorithm.

Plotting the Convergence:
We plot the value of the objective function over iterations to visualize how the algorithm converges

Output
Running Simulated Annealing...
Best solution found: x = -1.2742, f(x) = -3.3924
Time taken: 0.0742 seconds

"""

# Simulated Annealing Algorithm for Function Optimization
# Astro Pema Software (c)
# Oba Ozai 

import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np

def objective_function(x):
    """
    The objective function we want to minimize.
    """
    return x**2 + 4 * math.cos(2 * x)

def simulated_annealing(objective, initial_x, initial_temp, cooling_rate, num_iterations):
    """
    Simulated Annealing algorithm to minimize an objective function.
    
    Parameters:
    objective (function): The function to optimize.
    initial_x (float): Initial guess for the solution.
    initial_temp (float): Initial temperature.
    cooling_rate (float): Rate at which temperature decreases.
    num_iterations (int): Number of iterations to perform.
    
    Returns:
    float: Best solution found.
    """
    # Initialize variables
    current_x = initial_x
    current_temp = initial_temp
    best_x = current_x
    best_value = objective(current_x)

    # Store results for plotting
    history = []

    for i in range(num_iterations):
        # Generate a new candidate solution by perturbing the current solution
        new_x = current_x + random.uniform(-1, 1)
        new_value = objective(new_x)

        # Calculate the change in the objective function
        delta = new_value - best_value

        # Determine whether to accept the new solution
        if delta < 0 or random.random() < math.exp(-delta / current_temp):
            current_x = new_x
            best_value = new_value
            best_x = new_x

        # Cool down the temperature
        current_temp *= cooling_rate

        # Store the history for visualization
        history.append(best_value)

    return best_x, best_value, history

if __name__ == "__main__":
    # Start timer
    start_time = time.time()

    # Parameters
    initial_x = 0.0
    initial_temp = 100.0
    cooling_rate = 0.99
    num_iterations = 500

    print("Running Simulated Annealing...")
    
    # Run the simulated annealing algorithm
    best_x, best_value, history = simulated_annealing(objective_function, initial_x, initial_temp, cooling_rate, num_iterations)

    # End timer
    end_time = time.time()
    
    # Print results
    print(f"Best solution found: x = {best_x:.4f}, f(x) = {best_value:.4f}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    
    # Plot the convergence history
    plt.figure(figsize=(10, 6))
    plt.plot(history)
    plt.title("Simulated Annealing Optimization")
    plt.xlabel("Iteration")
    plt.ylabel("Objective Function Value")
    plt.grid(True)
    plt.show()

# EOF




 
