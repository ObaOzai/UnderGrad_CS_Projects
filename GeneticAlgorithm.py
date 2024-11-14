"""

Genetic Algorithms Overview

Genetic Algorithms (GAs) are optimization algorithms inspired by the process of natural selection and evolution.

They are used to find approximate solutions to optimization and search problems by mimicking the process of natural evolution.
GAs are particularly effective for complex, non-linear optimization problems where traditional methods might struggle.

Concept

Population: Start with a population of randomly generated solutions (chromosomes).
Fitness Function: Evaluate each solution's "fitness" to determine how good it is at solving the problem.
Selection: Select the fittest individuals to reproduce.
Crossover (Recombination): Combine two parents to produce new offspring.
Mutation: Apply random changes to the offspring to maintain genetic diversity.
Termination: Repeat the process until a stopping condition is met (e.g., a certain number of generations or an acceptable fitness level).

Example Problem

Let’s solve a classic optimization problem using a genetic algorithm:

We’ll maximize the function:

f(x)=x×sin(10πx)+1 where x is in the range [−1,2].

Genetic Operators:

Crossover: The offspring is the average of two parents.
Mutation: A small random change is applied to maintain diversity.
Selection: We select two parents based on their fitness scores using a weighted random choice.
Genetic Algorithm Process:
Generate an initial population.
Evaluate the fitness of each individual.
Create a new population through selection, crossover, and mutation.
Repeat for a specified number of generations.
We visualize the fitness over generations to see how the population evolves.

Output
Running Genetic Algorithm...
Best solution found: x = 1.1183, f(x) = 1.7558

"""

# Genetic Algorithm Example
# Astro Pema Software (c)
# Oba Ozai & ChatGPT4 Nov 2024

import random
import numpy as np
import matplotlib.pyplot as plt

# Define the fitness function
def fitness_function(x):
    return x * np.sin(10 * np.pi * x) + 1

# Generate a random individual (chromosome)
def generate_individual():
    return random.uniform(-1, 2)

# Create an initial population
def generate_population(size):
    return [generate_individual() for _ in range(size)]

# Perform crossover between two parents
def crossover(parent1, parent2):
    return (parent1 + parent2) / 2

# Perform mutation on an individual
def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        return individual + random.uniform(-0.1, 0.1)
    return individual

# Perform selection based on fitness
def select(population, fitness_scores):
    return random.choices(population, weights=fitness_scores, k=2)

# Genetic Algorithm
def genetic_algorithm(pop_size, generations, mutation_rate):
    # Generate initial population
    population = generate_population(pop_size)
    
    best_individuals = []
    
    for generation in range(generations):
        # Calculate fitness scores for the population
        fitness_scores = [fitness_function(ind) for ind in population]
        
        # Track the best individual
        best_individual = population[np.argmax(fitness_scores)]
        best_fitness = max(fitness_scores)
        best_individuals.append(best_fitness)
        
        # Generate a new population
        new_population = []
        for _ in range(pop_size // 2):
            # Select parents
            parent1, parent2 = select(population, fitness_scores)
            # Perform crossover
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            # Perform mutation
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            # Add children to the new population
            new_population.extend([child1, child2])
        
        population = new_population
    
    return best_individual, best_fitness, best_individuals

if __name__ == "__main__":
    # Parameters
    pop_size = 50
    generations = 100
    mutation_rate = 0.1

    print("Running Genetic Algorithm...")
    best_individual, best_fitness, fitness_history = genetic_algorithm(pop_size, generations, mutation_rate)
    
    print(f"Best solution found: x = {best_individual:.4f}, f(x) = {best_fitness:.4f}")
    
    # Plot the fitness history
    plt.figure(figsize=(10, 6))
    plt.plot(fitness_history)
    plt.title("Genetic Algorithm Optimization")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.grid(True)
    plt.show()

# EOF


