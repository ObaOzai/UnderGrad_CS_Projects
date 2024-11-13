"""
Fibonacci Sequence Overview
The Fibonacci Sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
Mathematically, it is defined as:

F(n)=F(n−1)+F(n−2)
with seed values:

F(0)=0,F(1)=1
The sequence looks like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Dynamic Programming is an efficient approach to calculate Fibonacci numbers, especially for large values of 
n. 

It avoids the redundant calculations seen in the naive recursive method.
Dynamic Programming Approach
Instead of recalculating the Fibonacci numbers repeatedly (as in the naive recursive solution), 
we store previously computed values in an array (or list) and reuse them. This reduces the time complexity to 

O(n) from O(n^2)

Explanation of the Code
Base Cases:
If n = 0 the function returns 0.
If n = 1 the function returns 1.

Dynamic Programming Array:
We initialize a list fib with the first two Fibonacci numbers: [0, 1].
We use a for loop to compute each subsequent Fibonacci number and store it in the list.
Iterative Calculation:
For each index 
i
i from 2 to n we calculate: fib[i] = fib[i - 1] + fib[i - 2]

Output

The 10-th Fibonacci number is: 55
First 15 Fibonacci numbers:
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
F(10) = 55
F(11) = 89
F(12) = 144
F(13) = 233
F(14) = 377

"""

# Fibonacci Sequence using Dynamic Programming
# Astro Pema Software (c)
# Oba Ozai Nov 2024

def fibonacci(n):
    """
    Function to calculate the n-th Fibonacci number using dynamic programming.
    
    Parameters:
    n (int): The position of the Fibonacci number to compute.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    # Edge cases for n = 0 or n = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Initialize the list to store Fibonacci numbers
    fib = [0, 1]
    
    # Calculate Fibonacci numbers iteratively and store them
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    
    return fib[n]

# Testing the Fibonacci function
if __name__ == "__main__":
    n = 10  # Change this value to compute a different Fibonacci number
    print(f"The {n}-th Fibonacci number is: {fibonacci(n)}")
    
    # Generate the first 15 Fibonacci numbers
    print("First 15 Fibonacci numbers:")
    for i in range(15):
        print(f"F({i}) = {fibonacci(i)}")

# EOF





