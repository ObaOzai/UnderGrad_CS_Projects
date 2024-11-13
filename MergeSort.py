"""

Merge Sort Overview

Merge Sort is a divide-and-conquer algorithm that splits a list into halves, recursively 
sorts each half, and then merges the sorted halves back together.
It is known for its efficiency and stability. It guarantees a time complexity of
O(nlog n)
O(nlog n) for all cases (best, average, and worst).


Unlike algorithms like Bubble Sort or Quick Sort, Merge Sort is particularly 
well-suited for large datasets due to its efficiency.

Explanation of the Code
Divide:
The list is divided into two halves using:
mid = len(arr) // 2
left_half = arr[:mid]
right_half = arr[mid:]

The merge_sort() function is then called recursively on both halves until the list cannot be divided further.
Conquer (Merge):
The merge() function takes two sorted lists (left and right) and merges them into a single sorted list.
The merging process involves comparing elements from both lists and inserting the smaller element into the original array.
Copy Remaining Elements:
After merging, if there are any remaining elements in either the left or right list, they are copied into the original array.

Output:
Original List: [38, 27, 43, 3, 9, 82, 10]
Sorted List: [3, 9, 10, 27, 38, 43, 82]
"""

# Merge Sort Algorithm
# Astro Pema Software (c)
# Oba Ozai Nov 2024

def merge_sort(arr):
    """
    Function to perform Merge Sort on a given list.
    """
    if len(arr) > 1:
        # Find the middle point of the list
        mid = len(arr) // 2
        
        # Divide the list into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left, right):
    """
    Helper function to merge two sorted lists into one sorted list.
    """
    i = j = k = 0

    # Merge the two halves into the original array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left half
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right half
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Testing the Merge Sort function
if __name__ == "__main__":
    # Sample list to be sorted
    sample_list = [38, 27, 43, 3, 9, 82, 10]
    print("Original List:", sample_list)
    
    merge_sort(sample_list)
    print("Sorted List:", sample_list)

# EOF


