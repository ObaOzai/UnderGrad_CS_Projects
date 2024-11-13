"""
Quick Sort Overview
Quick Sort is another popular divide-and-conquer algorithm that’s efficient for large datasets.
It works by selecting a "pivot" element, partitioning the list around the pivot such that elements less than the pivot are on the left and those greater than the pivot are on the right.
The algorithm then recursively sorts the left and right partitions.
Quick Sort generally has an average-case time complexity of 
O(n log n)
but in the worst case (when the smallest or largest element is always picked as the pivot), it can degrade to 
O(n^2)
However, with good pivot selection (like using the "median-of-three" method), 
it’s one of the fastest sorting algorithms in practice.

Explanation of the Code
Base Case:
If the list is empty or contains a single element, it’s already sorted, so we return it.
Pivot Selection:
In this implementation, we choose the last element as the pivot.
This can be adjusted to use different strategies like selecting the first element, the middle element, or even a random element to optimize performance.
Partitioning:
We create three separate lists:
left: Elements less than the pivot.
equal: Elements equal to the pivot.
right: Elements greater than the pivot.
Recursive Sorting:
We recursively sort the left and right lists and combine them with the equal list.

Output 
Original List: [33, 10, 59, 27, 25, 82, 11, 9, 42]
Sorted List: [9, 10, 11, 25, 27, 33, 42, 59, 82]

"""

# Quick Sort Algorithm
# Astro Pema Software (c)
# Oba Ozai Nov 2024

def quick_sort(arr):
    """
    Function to perform Quick Sort on a given list.
    """
    # Base case: If the list is empty or has one element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Select the pivot element (using the last element in the list)
    pivot = arr[-1]
    left = []   # Elements less than the pivot
    right = []  # Elements greater than the pivot
    equal = []  # Elements equal to the pivot (if there are duplicates)

    # Partition the list into left, equal, and right lists
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            equal.append(element)
    
    # Recursively apply quick_sort to the left and right partitions
    return quick_sort(left) + equal + quick_sort(right)

# Testing the Quick Sort function
if __name__ == "__main__":
    # Sample list to be sorted
    sample_list = [33, 10, 59, 27, 25, 82, 11, 9, 42]
    print("Original List:", sample_list)
    
    sorted_list = quick_sort(sample_list)
    print("Sorted List:", sorted_list)

# EOF


