# Bubble Sort Implementation in Python

def bubble_sort(arr):
    """
    Sorts a list using the bubble sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        swapped = False
        
        # Last i elements are already in their correct position
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps occurred, the array is already sorted
        if not swapped:
            break
    
    return arr


def bubble_sort_verbose(arr):
    """
    Bubble sort with step-by-step output for visualization.
    """
    n = len(arr)
    print(f"Original array: {arr}")
    
    for i in range(n):
        swapped = False
        print(f"\nPass {i + 1}:")
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  Swap: {arr}")
        
        if not swapped:
            print(f"  Array is sorted!")
            break
    
    return arr


# Test Case 1: Basic bubble sort
print("=" * 50)
print("Test Case 1: Basic Bubble Sort")
print("=" * 50)
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {numbers}")
result = bubble_sort(numbers.copy())
print(f"Sorted:   {result}")

# Test Case 2: Already sorted array
print("\n" + "=" * 50)
print("Test Case 2: Already Sorted Array")
print("=" * 50)
sorted_numbers = [1, 2, 3, 4, 5]
print(f"Original: {sorted_numbers}")
result = bubble_sort(sorted_numbers.copy())
print(f"Sorted:   {result}")

# Test Case 3: Reverse sorted array
print("\n" + "=" * 50)
print("Test Case 3: Reverse Sorted Array")
print("=" * 50)
reverse_numbers = [9, 7, 5, 3, 1]
print(f"Original: {reverse_numbers}")
result = bubble_sort(reverse_numbers.copy())
print(f"Sorted:   {result}")

# Test Case 4: With verbose output
print("\n" + "=" * 50)
print("Test Case 4: Verbose Output (Step-by-Step)")
print("=" * 50)
test_array = [5, 2, 8, 1, 9]
result = bubble_sort_verbose(test_array)
print(f"\nFinal sorted array: {result}")
