# Python List Sorting Examples

# Example 1: Sort a list of numbers in ascending order
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", numbers)
numbers.sort()
print("Sorted list (ascending):", numbers)

# Example 2: Sort a list in descending order
fruits = ["apple", "banana", "cherry", "date"]
print("\nOriginal list:", fruits)
fruits.sort(reverse=True)
print("Sorted list (descending):", fruits)

# Example 3: Using sorted() function (doesn't modify original)
mixed_numbers = [5, 2, 8, 1, 9]
print("\nOriginal list:", mixed_numbers)
sorted_list = sorted(mixed_numbers)
print("Sorted list (original unchanged):", mixed_numbers)
print("New sorted list:", sorted_list)

# Example 4: Sort list of tuples by second element
students = [("Alice", 85), ("Bob", 75), ("Charlie", 95)]
print("\nOriginal list of tuples:", students)
students.sort(key=lambda x: x[1])
print("Sorted by score:", students)

# Example 5: Sort list of dictionaries
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
print("\nOriginal list of dictionaries:", people)
people.sort(key=lambda x: x["age"])
print("Sorted by age:", people)
