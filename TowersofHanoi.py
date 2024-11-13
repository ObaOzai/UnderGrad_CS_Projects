"""

Towers of Hanoi Overview
The Towers of Hanoi is a classic recursive puzzle where you have three pegs and a number of disks of different sizes.
The goal is to move all the disks from the first peg to the third peg following these rules:
You can only move one disk at a time.
A larger disk cannot be placed on top of a smaller disk.
You can use the second peg as an auxiliary peg.
The puzzle has a time complexity of 

O(2 n−1), where n is the number of disks.
The minimum number of moves required to solve the puzzle is 
2n − 1

Explanation of the Code
Base Case:
If there is only one disk (n = 1
n=1), move it directly from the source peg to the target peg.

Recursive Steps: 
Step 1: Move n−1 disks from the source peg to the auxiliary peg.
Step 2: Move the nth (largest) disk from the source peg to the target peg.
Step 3: Move n−1 disks from the auxiliary peg to the target peg.

Recursive Nature:
The function calls itself twice for each step, reducing the problem size by 1 each time.

Output
When you run the code with 3 disks, you should see:

Solving Towers of Hanoi with 3 disks:
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C

"""

# Towers of Hanoi Algorithm
# Astro Pema Software (c)
# Oba Ozai Nov 2024

def towers_of_hanoi(n, source, auxiliary, target):
    """
    Function to solve the Towers of Hanoi puzzle.
    
    Parameters:
    n (int): Number of disks.
    source (str): The peg from which to move disks.
    auxiliary (str): The peg to use as an auxiliary.
    target (str): The peg to which disks should be moved.
    """
    if n == 1:
        # Base case: Move the last disk directly from source to target
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Step 1: Move n-1 disks from source to auxiliary peg
    towers_of_hanoi(n - 1, source, target, auxiliary)
    
    # Step 2: Move the nth disk from source to target peg
    print(f"Move disk {n} from {source} to {target}")
    
    # Step 3: Move n-1 disks from auxiliary peg to target peg
    towers_of_hanoi(n - 1, auxiliary, source, target)

# Testing the Towers of Hanoi function
if __name__ == "__main__":
    num_disks = 3  # Change this value to test with more disks
    print(f"Solving Towers of Hanoi with {num_disks} disks:")
    towers_of_hanoi(num_disks, 'A', 'B', 'C')

# EOF
