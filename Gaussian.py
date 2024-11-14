"""

Gaussian Elimination Overview
Gaussian Elimination is a method used to solve systems of linear equations. It transforms a system into an upper triangular matrix, which can then be solved using back-substitution.
It’s widely used in linear algebra, engineering, scientific computing, and numerical analysis.
Time Complexity: 

O(n^3), where n is the number of variables.

Concept

Form the augmented matrix from the system of equations.
Use row operations to convert the matrix into an upper triangular form.
Solve the system using back-substitution.

Explanation of the Code
Augmented Matrix:
We form the augmented matrix by concatenating A and b.

Forward Elimination:
For each row, we make the diagonal element 1 (normalizing the row).
We eliminate all entries below the pivot to form an upper triangular matrix.

Back-Substitution:
Once the matrix is in upper triangular form, we solve for each variable starting from the last row.

Output
Solving system of equations using Gaussian Elimination...
Solution:
x = 2.0000, y = -1.0000, z = 3.0000

"""

# Gaussian Elimination Algorithm
# Astro Pema Software (c)
# Oba Ozai - Nov 2024

import numpy as np

def gaussian_elimination(A, b):
    """
    Solve a system of linear equations using Gaussian Elimination.
    
    Parameters:
    A (ndarray): Coefficient matrix.
    b (ndarray): Constant terms vector.
    
    Returns:
    ndarray: Solution vector.
    """
    n = len(b)
    # Augment the matrix A with the vector b
    augmented_matrix = np.hstack([A, b.reshape(-1, 1)])

    # Forward elimination process
    for i in range(n):
        # Pivot: Make the diagonal element 1 by dividing the row
        pivot = augmented_matrix[i, i]
        if pivot == 0:
            raise ValueError("Matrix is singular or nearly singular")
        augmented_matrix[i] = augmented_matrix[i] / pivot
        
        # Eliminate the entries below the pivot
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i]
            augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]
    
    # Back-substitution process
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:n])
    
    return x

if __name__ == "__main__":
    # Coefficient matrix
    A = np.array([[2, 3, 1],
                  [4, 1, -3],
                  [3, 2, 2]], dtype=float)
    
    # Constant terms vector
    b = np.array([8, 2, 7], dtype=float)
    
    print("Solving system of equations using Gaussian Elimination...")
    solution = gaussian_elimination(A, b)
    
    print("Solution:")
    print(f"x = {solution[0]:.4f}, y = {solution[1]:.4f}, z = {solution[2]:.4f}")

# EOF


