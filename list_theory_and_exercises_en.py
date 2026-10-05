"""
================================================================================
               COMPREHENSIVE GUIDE TO PYTHON LISTS (FULL ENGLISH)
                     (THEORY + BUILT-IN METHODS + 10 EXERCISES)
================================================================================
"""

# ==============================================================================
# PART 1: OVERVIEW OF PYTHON LISTS
# ==============================================================================
"""
1. Concept:
   - A List is a sequence data type used to store a collection of items.
   - Key Characteristics:
     + Ordered: Elements maintain their defined insertion order.
     + Mutable: You can add, modify, or remove elements after creation.
     + Allows Duplicates: Multiple elements can have identical values.
     + Heterogeneous: Can hold mixed data types (int, float, str, bool, nested lists, etc.).

2. List Initialization:
"""
empty_list_1 = []                  # Method 1 to initialize an empty list
empty_list_2 = list()              # Method 2 using list() constructor
fruits = ["Apple", "Banana", "Orange", "Mango"]
mixed_list = [10, "Hello", 3.14, True, [1, 2, 3]]
numbers = list(range(1, 6))        # Creates [1, 2, 3, 4, 5]


# ==============================================================================
# PART 2: ELEMENT ACCESS & SLICING TECHNIQUES
# ==============================================================================
"""
Slicing Syntax: list[start : stop : step]
- start: Starting index (default is 0).
- stop : Ending index (exclusive, stops before this index).
- step : Step size / stride (default is 1).
"""
nums = [10, 20, 30, 40, 50, 60, 70, 80]

# Indexing
first_item = nums[0]        # 10 (Positive index from left: 0, 1, 2,...)
last_item = nums[-1]        # 80 (Negative index from right: -1, -2, -3,...)

# Slicing
sub_1 = nums[1:5]           # [20, 30, 40, 50] (From index 1 up to 4)
sub_2 = nums[:3]            # [10, 20, 30] (From start to index 2)
sub_3 = nums[4:]            # [50, 60, 70, 80] (From index 4 to end)
sub_4 = nums[::2]           # [10, 30, 50, 70] (Every 2nd element)
reversed_nums = nums[::-1]  # [80, 70, 60, 50, 40, 30, 20, 10] (Reversed list)


# ==============================================================================
# PART 3: BUILT-IN LIST METHODS
# ==============================================================================

my_list = [1, 2, 3]

# 1. Adding Elements:
# - append(x): Appends element x to the end of the list
my_list.append(4)               # [1, 2, 3, 4]

# - insert(index, x): Inserts element x at the specified index
my_list.insert(1, 99)           # [1, 99, 2, 3, 4]

# - extend(iterable): Appends elements from an iterable to the end
my_list.extend([5, 6])          # [1, 99, 2, 3, 4, 5, 6]

# 2. Removing Elements:
# - remove(x): Removes the first occurrence of item x (raises ValueError if not found)
my_list.remove(99)              # [1, 2, 3, 4, 5, 6]

# - pop(index): Removes and returns item at index (defaults to index=-1, the last item)
last = my_list.pop()            # Removes 6, my_list becomes [1, 2, 3, 4, 5]
item_at_0 = my_list.pop(0)      # Removes 1, my_list becomes [2, 3, 4, 5]

# - del: Keyword to delete item by index or slice
del my_list[0]                  # Removes item at index 0

# - clear(): Removes all elements from the list
my_list.clear()                 # my_list becomes []

# 3. Searching & Counting:
sample = [10, 20, 30, 20, 40, 20]

# - index(x): Returns the index of the first occurrence of x
pos = sample.index(20)          # 1

# - count(x): Returns the number of occurrences of x
cnt = sample.count(20)          # 3

# - Membership operators: in / not in
has_30 = 30 in sample           # True
has_99 = 99 in sample           # False

# 4. Sorting & Reversing:
scores = [50, 20, 90, 10, 40]

# - sort(key=None, reverse=False): Sorts the list in-place
scores.sort()                   # [10, 20, 40, 50, 90] (Ascending)
scores.sort(reverse=True)       # [90, 50, 40, 20, 10] (Descending)

# - sorted(list): Returns a NEW sorted list, leaves original list unchanged
original = [3, 1, 2]
new_sorted = sorted(original)   # original is [3, 1, 2], new_sorted is [1, 2, 3]

# - reverse(): Reverses the list elements in-place
scores.reverse()

# 5. Copying a List:
# - copy(): Creates a shallow copy of the list
list_a = [1, 2, 3]
list_b = list_a.copy()          # Or list_b = list_a[:]


# ==============================================================================
# PART 4: COMMON BUILT-IN FUNCTIONS WITH LISTS
# ==============================================================================
arr = [5, 2, 9, 1, 7]

length = len(arr)               # 5: Number of elements
minimum = min(arr)              # 1: Smallest element
maximum = max(arr)              # 9: Largest element
total = sum(arr)                # 24: Sum of all elements


# ==============================================================================
# PART 5: LIST ITERATION & LIST COMPREHENSION
# ==============================================================================

animals = ["Dog", "Cat", "Bird"]

# Method 1: Direct item iteration
for animal in animals:
    pass

# Method 2: Index-based iteration using range(len(...))
for i in range(len(animals)):
    pass

# Method 3: Both index and value using enumerate()
for idx, val in enumerate(animals):
    pass

# List Comprehension (Concise syntax for creating lists):
# Syntax: [expression for item in iterable if condition]
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# Result: [4, 16, 36, 64, 100]


# ==============================================================================
# PART 6: 10 PRACTICAL EXERCISES WITH COMPLETE SOLUTIONS
# ==============================================================================

print("\n" + "=" * 60)
print("             10 PRACTICAL LIST EXERCISES & SOLUTIONS")
print("=" * 60 + "\n")

# ------------------------------------------------------------------------------
# EXERCISE 1: Calculate the Sum and Average of an Integer List
# ------------------------------------------------------------------------------
print("--- EXERCISE 1: SUM AND AVERAGE ---")
ex1_list = [12, 45, 67, 23, 89, 34]
total_ex1 = sum(ex1_list)
avg_ex1 = total_ex1 / len(ex1_list) if len(ex1_list) > 0 else 0
print(f"List: {ex1_list}")
print(f"Sum = {total_ex1}, Average = {avg_ex1:.2f}\n")


# ------------------------------------------------------------------------------
# EXERCISE 2: Find Maximum, Minimum Values and Their Indices
# ------------------------------------------------------------------------------
print("--- EXERCISE 2: FIND MAX, MIN AND THEIR INDICES ---")
ex2_list = [29, 10, 85, 4, 63, 85, 7]
max_val = max(ex2_list)
min_val = min(ex2_list)
max_idx = ex2_list.index(max_val)
min_idx = ex2_list.index(min_val)
print(f"List: {ex2_list}")
print(f"Max: {max_val} (at index {max_idx})")
print(f"Min: {min_val} (at index {min_idx})\n")


# ------------------------------------------------------------------------------
# EXERCISE 3: Count and Separate Even and Odd Numbers
# ------------------------------------------------------------------------------
print("--- EXERCISE 3: COUNT AND SEPARATE EVEN / ODD ---")
ex3_list = [1, 4, 7, 8, 10, 13, 16, 19, 22]
even_nums = [x for x in ex3_list if x % 2 == 0]
odd_nums = [x for x in ex3_list if x % 2 != 0]
print(f"Original List: {ex3_list}")
print(f"Even numbers ({len(even_nums)}): {even_nums}")
print(f"Odd numbers ({len(odd_nums)}): {odd_nums}\n")


# ------------------------------------------------------------------------------
# EXERCISE 4: Remove Duplicates While Preserving Original Order
# ------------------------------------------------------------------------------
print("--- EXERCISE 4: REMOVE DUPLICATES ---")
ex4_list = [1, 3, 2, 3, 4, 1, 5, 2, 6, 4]
unique_list = []
for item in ex4_list:
    if item not in unique_list:
        unique_list.append(item)
print(f"Original List: {ex4_list}")
print(f"After Removing Duplicates: {unique_list}\n")


# ------------------------------------------------------------------------------
# EXERCISE 5: Separate Negative and Non-Negative Numbers
# ------------------------------------------------------------------------------
print("--- EXERCISE 5: SEPARATE NEGATIVE AND NON-NEGATIVE ---")
ex5_list = [-10, 15, -3, 0, 22, -8, 7, -1]
negative_nums = [x for x in ex5_list if x < 0]
non_negative_nums = [x for x in ex5_list if x >= 0]
print(f"List: {ex5_list}")
print(f"Negative numbers: {negative_nums}")
print(f"Non-negative numbers: {non_negative_nums}\n")


# ------------------------------------------------------------------------------
# EXERCISE 6: Reverse a List Manually (Without Using reverse() or [::-1])
# ------------------------------------------------------------------------------
print("--- EXERCISE 6: CUSTOM LIST REVERSAL ALGORITHM ---")
ex6_list = [10, 20, 30, 40, 50]
custom_reversed = []
for i in range(len(ex6_list) - 1, -1, -1):
    custom_reversed.append(ex6_list[i])
print(f"Original List: {ex6_list}")
print(f"Reversed List: {custom_reversed}\n")


# ------------------------------------------------------------------------------
# EXERCISE 7: Find Elements Appearing More Than k Times
# ------------------------------------------------------------------------------
print("--- EXERCISE 7: FIND ELEMENTS OCCURRING > K TIMES ---")
ex7_list = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]
k = 2
result_ex7 = []
for item in set(ex7_list):
    if ex7_list.count(item) > k:
        result_ex7.append(item)
print(f"List: {ex7_list}")
print(f"Elements occurring more than {k} times: {result_ex7}\n")


# ------------------------------------------------------------------------------
# EXERCISE 8: Find the Second Largest Number in a List
# ------------------------------------------------------------------------------
print("--- EXERCISE 8: FIND SECOND LARGEST NUMBER ---")
ex8_list = [15, 30, 45, 45, 20, 10]
# Remove duplicates first so duplicate maximum values do not interfere
unique_sorted = sorted(list(set(ex8_list)), reverse=True)
second_largest = unique_sorted[1] if len(unique_sorted) > 1 else None
print(f"List: {ex8_list}")
print(f"Second largest number: {second_largest}\n")


# ------------------------------------------------------------------------------
# EXERCISE 9: Insert x into a Sorted List to Keep it Sorted
# ------------------------------------------------------------------------------
print("--- EXERCISE 9: INSERT X INTO SORTED LIST ---")
ex9_list = [10, 20, 30, 40, 50]
x = 25
inserted = False
for i in range(len(ex9_list)):
    if ex9_list[i] > x:
        ex9_list.insert(i, x)
        inserted = True
        break
if not inserted:
    ex9_list.append(x)
print(f"After inserting x = {x}: {ex9_list}\n")


# ------------------------------------------------------------------------------
# EXERCISE 10: Simple Student List Management Application (Add, Remove, Search)
# ------------------------------------------------------------------------------
print("--- EXERCISE 10: STUDENT LIST MANAGEMENT ---")
students = ["Alice", "Bob", "Charlie", "David"]
print(f"Initial student list: {students}")

# Add new student
students.append("Emma")
print(f"After adding Emma: {students}")

# Remove student Bob if present
if "Bob" in students:
    students.remove("Bob")
    print(f"After removing Bob: {students}")

# Search for index of "Charlie"
search_name = "Charlie"
if search_name in students:
    pos = students.index(search_name)
    print(f"Found '{search_name}' at index: {pos}")
else:
    print(f"'{search_name}' not found in list")

# Sort list alphabetically (A-Z)
students.sort()
print(f"List after sorting A-Z: {students}")
