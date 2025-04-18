"""
Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, 
and swaps them if they are in the wrong order. The process repeats until no more swaps are needed, 
indicating that the list is sorted.

It has a time complexity of 
O(n2)
O(n2) 

in the worst and average cases, making it inefficient for large lists, but it's a great 
starting point to understand sorting concepts.

Explanation of the Code

Outer Loop: The outer loop runs through the list multiple times. With each pass, the largest unsorted element "bubbles up" to its correct position.
Inner Loop: The inner loop performs pairwise comparisons and swaps elements if they are out of order.
Optimization with swapped Flag:
If no elements were swapped during a pass, it means the list is already sorted, and the algorithm can terminate early.
Testing:
The script includes a sample list [64, 34, 25, 12, 22, 11, 90] which is sorted using the bubble_sort() function.

Original List: [64, 34, 25, 12, 22, 11, 90]
Sorted List: [11, 12, 22, 25, 34, 64, 90]
"""
# Bubble Sort Algorithm
# Astro Pema Software (c)
# Oba Ozai Nov 2024

def bubble_sort(arr):
    """
    Function to perform Bubble Sort on a given list.
    """
    n = len(arr)
    # Outer loop to traverse through the entire list
    for i in range(n):
        # A flag to check if any swaps happened in this pass
        swapped = False
        
        # Inner loop to perform the pairwise comparison and swapping
        for j in range(0, n - i - 1):
            # If the current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps were made in the inner loop, the list is sorted
        if not swapped:
            break

    return arr

# Testing the Bubble Sort function
if __name__ == "__main__":
    # Sample list to be sorted
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original List:", sample_list)
    
    sorted_list = bubble_sort(sample_list)
    print("Sorted List:", sorted_list)

# EOF

