"""

Binary Search Overview
Binary Search is an efficient algorithm for finding an element in a sorted list.
It works by repeatedly dividing the search interval in half.
If the target value is less than the middle element, it searches the left half. Otherwise, it searches the right half.
The process continues until the target element is found or the search interval is empty.
Time Complexity: 
O(log n)

Explanation of the Code
Initialization:
The search range is defined using two pointers: left (starting at the beginning) and right (starting at the end).
Finding the Middle Element:

The middle index is calculated as:
mid = (left + right) // 2

Decision Making:
If the middle element matches the target, we return its index.
If the target is smaller, the search continues in the left half:
right = mid - 1

If the target is larger, the search continues in the right half:
left = mid + 1

Stopping Condition:
The loop stops when left exceeds right, meaning the target is not in the list.
Output
Searching for 21 in the list...
Checking middle element at index 4: 14
Target is greater than 14, searching right half.
Checking middle element at index 7: 24
Target is less than 24, searching left half.
Checking middle element at index 6: 21
Target 21 found at index 6.

# Binary Search Algorithm
# Astro Pema Software (c)
# Oba Ozai Nov 2024

def binary_search(arr, target):
    """
    Perform binary search on a sorted list to find the target value.
    
    Parameters:
    arr (list): The sorted list to search in.
    target (int): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    # Define the initial left and right pointers
    left, right = 0, len(arr) - 1

    while left <= right:
        # Find the middle element
        mid = (left + right) // 2
        print(f"Checking middle element at index {mid}: {arr[mid]}")

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Target found, return the index
        
        # If target is less than the middle element, search in the left half
        elif arr[mid] > target:
            print(f"Target is less than {arr[mid]}, searching left half.")
            right = mid - 1

        # If target is greater than the middle element, search in the right half
        else:
            print(f"Target is greater than {arr[mid]}, searching right half.")
            left = mid + 1

    # Target not found
    return -1

# Testing the Binary Search function
if __name__ == "__main__":
    # A sorted list to search in
    sorted_list = [3, 6, 8, 12, 14, 18, 21, 24, 27, 30]
    target_value = 21

    print(f"Searching for {target_value} in the list...")
    result_index = binary_search(sorted_list, target_value)

    if result_index != -1:
        print(f"Target {target_value} found at index {result_index}.")
    else:
        print(f"Target {target_value} not found in the list.")

# EOF


