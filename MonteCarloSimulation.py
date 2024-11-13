"""

Monte Carlo Simulation - Estimating π (Pi)
One of the simplest yet classic applications of Monte Carlo methods is estimating the value of π using random sampling.

Concept
Imagine a square with an inscribed circle. If we randomly throw darts at this square, some of them will land inside the circle, 
and some will land outside. The ratio of darts that land inside the circle to the total number of darts thrown can be used to estimate π, since:

π = ((Area of Circle) / (Area of Square) × 4

The area of the circle is 
π * r^2

the area of the square is 
(2r)^2

For simplicity, let’s assume r=1
the square has an area of 4 and the circle has an area of π.

Memory updated
Perfect, Pema! We'll tackle these one by one, just like before. Let’s start with our first project: Monte Carlo Simulations.

Monte Carlo Simulation - Estimating π (Pi)
One of the simplest yet classic applications of Monte Carlo methods is estimating the value of π using random sampling.

Explanation of the Code
Generating Random Points:
We generate random points within the square using random.uniform(-1, 1) for both 
x and y coordinates.
Counting Points Inside the Circle:
We check if a point lies within the circle using the equation:
x^2 + y^2 ≤ 1

If true, it means the point is inside the circle.

Estimating π:
The ratio of points inside the circle to the total number of points, multiplied by 4, 
gives an estimate of π.

Measuring Time:
We use time.time() to measure how long the simulation takes.


"""

# Monte Carlo Simulation to Estimate Pi
# Astro Pema Software (c)
# Oba Ozai & ChatGPT4 Nov 2024

import random
import time

def estimate_pi(num_points):
    """
    Function to estimate the value of π using Monte Carlo simulation.
    
    Parameters:
    num_points (int): Number of random points to generate.
    
    Returns:
    float: Estimated value of π.
    """
    inside_circle = 0

    for _ in range(num_points):
        # Generate random (x, y) coordinates between -1 and 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Check if the point is inside the circle
        if x**2 + y**2 <= 1:
            inside_circle += 1

    # Estimate of π
    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate

if __name__ == "__main__":
    # Start the timer
    start_time = time.time()
    
    # Number of points to generate
    num_points = 1000000  # Adjust this value for more accuracy
    print(f"Estimating π using {num_points} random points...")
    
    # Estimate π
    pi_value = estimate_pi(num_points)
    
    # End the timer
    end_time = time.time()
    
    # Print the results
    print(f"Estimated value of π: {pi_value}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")

# EOF
