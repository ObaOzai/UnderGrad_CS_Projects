"""

Monte Carlo Simulation - Stock Price Forecasting
Monte Carlo simulations can be used to predict future stock prices by simulating different 
possible price movements based on historical data. 
This technique helps estimate potential future returns and assess risk.

Concept
We assume that stock prices follow a geometric Brownian motion (a continuous-time stochastic process).

Ref link
https://en.wikipedia.org/wiki/Monte_Carlo_methods_in_finance#:~:text=In%20finance%2C%20the%20Monte%20Carlo,values%20of%20the%20underlying%20inputs.

S subs tmis the current stock price.
μ is the expected return (mean of historical returns).
σ is the volatility (standard deviation of historical returns).
Δt is the time step (usually set to 1 day).
Z is a random variable drawn from a standard normal distribution (
N(0,1)).

Explanation of the Code
Simulation Initialization:
We create a 2D array simulations to store the results of each simulation.
Stock Price Calculation:
For each simulation, we generate stock prices over num_days using the formula:

<ecuation ommited>

Z is a random number from a normal distribution.
Plotting the Results:
The results of all simulations are plotted to visualize potential future stock prices.

Measuring Time:
We use time.time() to measure how long the simulations take.


Output
the code, it will generate a plot similar to this:

The plot shows multiple lines representing different possible paths for the stock price over a year (252 trading days).
Each line represents one simulation, and the spread of lines shows the range of possible future prices.

pip install numpy pandas matplotlib


Try changing the initial stock price (S0), expected return (mu), volatility (sigma), number of simulations,
and number of days to see how the forecast changes.

Experiment with higher volatility values to observe how the spread of potential outcomes widens.

"""

# Monte Carlo Simulation for Stock Price Forecasting
# Astro Pema Software (c)
# Oba Ozai & ChatGPT4 Nov 2024

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def monte_carlo_simulation(S0, mu, sigma, num_simulations, num_days):
    """
    Monte Carlo simulation to predict future stock prices.
    
    Parameters:
    S0 (float): Initial stock price.
    mu (float): Expected return.
    sigma (float): Volatility of the stock.
    num_simulations (int): Number of simulations to run.
    num_days (int): Number of days to simulate.
    
    Returns:
    np.ndarray: Simulated stock prices.
    """
    # Initialize an array to store the results
    simulations = np.zeros((num_simulations, num_days))
    
    for i in range(num_simulations):
        # Set the first value as the initial stock price
        prices = [S0]
        for _ in range(1, num_days):
            # Generate a random number from a normal distribution
            Z = np.random.normal()
            # Calculate the new price
            new_price = prices[-1] * np.exp((mu - 0.5 * sigma**2) + sigma * Z)
            prices.append(new_price)
        simulations[i, :] = prices
    
    return simulations

if __name__ == "__main__":
    # Start timer
    start_time = time.time()
    
    # Parameters for the simulation
    S0 = 100  # Initial stock price
    mu = 0.0002  # Expected return (daily)
    sigma = 0.01  # Volatility (daily)
    num_simulations = 1000  # Number of simulations
    num_days = 252  # Number of days (1 trading year)
    
    print("Running Monte Carlo simulations...")
    
    # Run the simulation
    simulations = monte_carlo_simulation(S0, mu, sigma, num_simulations, num_days)
    
    # Plot the simulation results
    plt.figure(figsize=(10, 6))
    plt.plot(simulations.T, alpha=0.1)
    plt.title("Monte Carlo Simulation of Stock Prices")
    plt.xlabel("Days")
    plt.ylabel("Stock Price")
    plt.grid(True)
    plt.show()
    
    # End timer
    end_time = time.time()
    print(f"Simulations completed in {end_time - start_time:.4f} seconds")

# EOF




