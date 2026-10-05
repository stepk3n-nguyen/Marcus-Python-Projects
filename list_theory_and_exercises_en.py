"""
================================================================================
               COMPREHENSIVE GUIDE TO PYTHON LISTS (FULL ENGLISH)
                 THEORY + STEP-BY-STEP SOLUTION GUIDES + 10 EXERCISES
================================================================================

This file serves as both an educational textbook and an executable Python script.
It covers:
  - Part 1: Overview and Core Theory of Python Lists
  - Part 2: Element Access, Indexing, and Slicing Mechanics
  - Part 3: Built-in List Methods (In-depth analysis & memory behavior)
  - Part 4: Common Built-in Functions Used with Lists
  - Part 5: List Iteration Patterns & List Comprehensions
  - Part 6: 10 Practical Exercises with Step-by-Step Solution Guides & Code
"""

# ==============================================================================
# PART 1: OVERVIEW AND CORE THEORY OF PYTHON LISTS
# ==============================================================================
"""
--- 1. WHAT IS A PYTHON LIST? ---
A List is a built-in sequence data structure in Python designed to store an ordered
collection of items. Under the hood, a Python list is implemented as a dynamic array
of pointers (references). This means the list itself does not store the raw object
data contiguously; rather, it stores memory references pointing to where each object
resides in memory.

--- 2. CORE CHARACTERISTICS ---
1. Ordered:
   The elements in a list have a definite, preserved order. If you insert items in
   the sequence A, B, C, they will remain at indices 0, 1, and 2 unless you explicitly
   reorder or modify the list.

2. Mutable (Changeable):
   Lists are mutable. You can add new items, modify existing items, or remove items
   in-place without creating an entirely new list object in memory. This is a critical
   distinction from immutable sequences like strings or tuples.

3. Heterogeneous (Mixed Data Types):
   Because lists store references, a single list can contain elements of diverse data
   types: integers, floating-point numbers, strings, booleans, functions, and even
   other nested lists or dictionaries.

4. Dynamic Resizing:
   Unlike arrays in static languages (e.g., C, Java) where size is fixed upon creation,
   Python lists automatically grow and shrink as items are added or removed.

5. Allows Duplicate Values:
   Lists do not enforce uniqueness. The exact same value can appear multiple times
   at different index positions.

--- 3. INITIALIZATION TECHNIQUES ---
There are multiple ways to construct a list in Python:
"""

# Approach 1: Empty list using square bracket literals (Recommended & faster)
empty_list_1 = []

# Approach 2: Empty list using the list() constructor
empty_list_2 = list()

# Approach 3: List initialized with homogeneous values (strings)
fruits = ["Apple", "Banana", "Orange", "Mango"]

# Approach 4: Heterogeneous list containing multiple distinct data types
# Elements: integer (10), string ("Hello"), float (3.14), boolean (True), nested list ([1, 2, 3])
mixed_list = [10, "Hello", 3.14, True, [1, 2, 3]]

# Approach 5: Initializing from a range sequence
# Converts range(1, 6) into [1, 2, 3, 4, 5]
numbers = list(range(1, 6))

# Approach 6: Repeated element list initialization using the multiplication operator
# Creates a list of five zeros: [0, 0, 0, 0, 0]
zeros = [0] * 5


# ==============================================================================
# PART 2: ELEMENT ACCESS, INDEXING, AND SLICING MECHANICS
# ==============================================================================
"""
--- 1. INDEXING (0-BASED & NEGATIVE) ---
Every item in a list has an assigned integer position called an index:
- Positive Indexing (Left-to-Right): Starts at 0 for the first element and increments
  up to len(list) - 1 for the final element.
- Negative Indexing (Right-to-Left): Starts at -1 for the last element, -2 for the
  second-to-last element, down to -len(list) for the first element.

ATTENTION / PITFALL:
Accessing an index that does not exist (e.g., index >= len(list)) triggers an
IndexError: list index out of range. Always ensure the index is within valid bounds.

--- 2. SLICING MECHANICS ---
Slicing retrieves a sub-list (a brand new copy) based on a range:
Syntax: list[start : stop : step]

Parameters:
- start : The index where the slice begins (INCLUSIVE). Defaults to 0 if step > 0.
- stop  : The index where the slice terminates (EXCLUSIVE - stops right before this).
          Defaults to len(list) if step > 0.
- step  : The stride / increment between elements. Defaults to 1.
          If step is negative, traversal moves backward (right-to-left).

KEY ADVANTAGE OF SLICING:
Unlike direct indexing, slicing NEVER raises an IndexError if start or stop exceed
list boundaries. Python automatically clamps out-of-range bounds to valid boundaries.
"""

nums = [10, 20, 30, 40, 50, 60, 70, 80]

# Direct Indexing examples:
first_item = nums[0]        # Output: 10 (First item at index 0)
last_item = nums[-1]        # Output: 80 (Last item at index -1)
second_last = nums[-2]      # Output: 70 (Second-to-last item)

# Slicing examples:
sub_1 = nums[1:5]           # [20, 30, 40, 50] (Extracts indices 1, 2, 3, 4; stops before 5)
sub_2 = nums[:3]            # [10, 20, 30] (From index 0 up to index 2)
sub_3 = nums[4:]            # [50, 60, 70, 80] (From index 4 through the end)
sub_4 = nums[::2]           # [10, 30, 50, 70] (Every second element from start to end)
reversed_nums = nums[::-1]  # [80, 70, 60, 50, 40, 30, 20, 10] (Complete backward slice)


# ==============================================================================
# PART 3: BUILT-IN LIST METHODS (THEORY & RUNTIME BEHAVIOR)
# ==============================================================================
"""
List methods allow direct manipulation of list contents. Understanding their behavior,
return values, and time complexity is essential for writing efficient code.

1. ADDING ELEMENTS:
   - append(x)       : Adds item x to the very end. O(1) amortized time.
                       Modifies the list in-place and returns None.
   - insert(index, x): Inserts item x at the specified index. All elements at and after
                       this position are shifted one position to the right. O(n) time.
   - extend(iterable): Unpacks the given iterable (list, tuple, etc.) and appends each
                       item individually to the end. O(k) time where k is iterable length.

2. REMOVING ELEMENTS:
   - remove(x)       : Finds and deletes the FIRST occurrence of value x.
                       Raises ValueError if x is not found in the list.
   - pop([index])    : Removes and RETURNS the item at the specified index.
                       Defaults to index=-1 (the last item, O(1) time).
                       If popping index 0, subsequent items shift left (O(n) time).
   - del statement   : Built-in Python statement (del list[index] or del list[start:stop])
                       to remove elements by index or slice without returning a value.
   - clear()         : Empties the list completely in-place. Length becomes 0.

3. SEARCHING & COUNTING:
   - index(x)        : Returns the 0-based index of the first occurrence of x.
                       Raises ValueError if x is missing.
   - count(x)        : Returns the total count of times x occurs in the list.
                       Returns 0 if x is not present.
   - in / not in     : Membership test operator. Returns True or False. Runs in O(n) time.

4. SORTING & REVERSING:
   - sort() vs sorted():
     * list.sort(key=None, reverse=False): Sorts the list IN-PLACE using Timsort
       (O(n log n)). It modifies the original list and returns None.
     * sorted(iterable): Returns a BRAND NEW sorted list while leaving the original
       list unchanged.
   - reverse()       : Inverts the order of elements in-place in O(n) time.

5. COPYING & MEMORY ALIASING PITFALL:
   - Aliasing: writing 'list_b = list_a' does NOT copy the list! It merely creates
     a second reference pointing to the identical list in memory. Changing list_b
     will inadvertently alter list_a.
   - Shallow Copy: 'list_b = list_a.copy()' or 'list_a[:]' creates an independent
     outer list container.
"""

my_list = [1, 2, 3]

# 1. Adding Elements:
my_list.append(4)               # Result: [1, 2, 3, 4]
my_list.insert(1, 99)           # Result: [1, 99, 2, 3, 4] (Inserts 99 at index 1)
my_list.extend([5, 6])          # Result: [1, 99, 2, 3, 4, 5, 6]

# 2. Removing Elements:
my_list.remove(99)              # Result: [1, 2, 3, 4, 5, 6] (Removes first 99)
last = my_list.pop()            # Returns 6; my_list becomes [1, 2, 3, 4, 5]
item_at_0 = my_list.pop(0)      # Returns 1; my_list becomes [2, 3, 4, 5]
del my_list[0]                  # Removes item at index 0 (2); my_list becomes [3, 4, 5]
my_list.clear()                 # Empties the list; my_list becomes []

# 3. Searching & Counting:
sample = [10, 20, 30, 20, 40, 20]
pos = sample.index(20)          # Output: 1 (Index of first occurrence of 20)
cnt = sample.count(20)          # Output: 3 (20 occurs 3 times)
has_30 = 30 in sample           # Output: True
has_99 = 99 in sample           # Output: False

# 4. Sorting & Reversing:
scores = [50, 20, 90, 10, 40]
scores.sort()                   # In-place ascending: [10, 20, 40, 50, 90]
scores.sort(reverse=True)       # In-place descending: [90, 50, 40, 20, 10]

original = [3, 1, 2]
new_sorted = sorted(original)   # original stays [3, 1, 2]; new_sorted is [1, 2, 3]
scores.reverse()                # Reverses the elements of scores in-place

# 5. Copying:
list_a = [1, 2, 3]
list_b = list_a.copy()          # Safe shallow copy; list_b is independent of list_a


# ==============================================================================
# PART 4: COMMON BUILT-IN FUNCTIONS USED WITH LISTS
# ==============================================================================
"""
Python provides several global built-in functions that operate on lists:
- len(list) : Returns the number of items. Runs in O(1) time because Python stores
              the element count inside the list header struct.
- min(list) : Returns the minimum element. Requires all elements to be comparable.
- max(list) : Returns the maximum element.
- sum(list) : Calculates the arithmetic sum of numbers. Optional second argument
              specifies a start value (e.g., sum(list, 10)).
- all(list) : Returns True if every element evaluates to truthy (non-zero, non-empty).
- any(list) : Returns True if at least one element evaluates to truthy.
"""

arr = [5, 2, 9, 1, 7]
length = len(arr)               # 5
minimum = min(arr)              # 1
maximum = max(arr)              # 9
total = sum(arr)                # 24 (5 + 2 + 9 + 1 + 7)


# ==============================================================================
# PART 5: LIST ITERATION PATTERNS & LIST COMPREHENSIONS
# ==============================================================================
"""
--- 1. ITERATION PATTERNS ---
1. Item-based Iteration (for item in list):
   The most Pythonic and readable approach when index values are not required.

2. Index-based Iteration (for i in range(len(list))):
   Useful when you need to reassign or modify elements in-place by their index.

3. Enumerate Iteration (for idx, val in enumerate(list)):
   Provides both the index and the value simultaneously in an elegant manner.

--- 2. LIST COMPREHENSION ---
List comprehension provides a concise, declarative syntax to construct a new list
by applying an expression to each item of an iterable, optionally filtering with an if clause.

Syntax:
    [expression for item in iterable if condition]

Why use List Comprehension?
1. More readable and expressive than multi-line loops with .append().
2. Faster execution speed due to C-level optimizations in the Python interpreter.
"""

animals = ["Dog", "Cat", "Bird"]

# Pattern 1: Direct item iteration
for animal in animals:
    pass

# Pattern 2: Index-based iteration
for i in range(len(animals)):
    pass

# Pattern 3: Both index and value using enumerate()
for idx, val in enumerate(animals):
    pass

# List Comprehension Example:
# Squares of all even numbers from 1 to 10
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# Result: [4, 16, 36, 64, 100]


# ==============================================================================
# PART 6: 10 PRACTICAL EXERCISES WITH STEP-BY-STEP SOLUTION GUIDES & CODE
# ==============================================================================

print("\n" + "=" * 70)
print("       10 PRACTICAL LIST EXERCISES WITH COMPREHENSIVE SOLUTION GUIDES")
print("=" * 70 + "\n")


# ------------------------------------------------------------------------------
# EXERCISE 1: Calculate the Sum and Average of an Integer List
# ------------------------------------------------------------------------------
"""
[PROBLEM DESCRIPTION]
Given a list of integers, calculate and print:
1. The total sum of all elements.
2. The arithmetic average (mean) rounded to 2 decimal places.

[STEP-BY-STEP SOLUTION GUIDE & THOUGHT PROCESS]
1. Finding the Sum:
   - Python provides a built-in sum() function that iterates through the list and
     accumulates the total in O(n) time.
2. Finding the Number of Elements:
   - Use len() to retrieve the total count of elements in O(1) time.
3. Calculating the Average:
   - The formula for the arithmetic mean is: average = total_sum / count.
4. Handling Edge Cases:
   - Division by zero: If the list is empty (len == 0), dividing by len will throw
     a ZeroDivisionError. Therefore, use a conditional ternary operator:
     avg = total / len if len > 0 else 0.
5. Displaying Results:
   - Use Python f-strings with the format specifier ':.2f' to format the floating-point
     average to 2 decimal places.
"""
print("--- EXERCISE 1: SUM AND AVERAGE ---")
ex1_list = [12, 45, 67, 23, 89, 34]

# Step 1: Compute total sum using the built-in sum() function
total_ex1 = sum(ex1_list)

# Step 2: Compute average with a zero-division guard
avg_ex1 = total_ex1 / len(ex1_list) if len(ex1_list) > 0 else 0.0

# Step 3: Print formatted output
print(f"List: {ex1_list}")
print(f"Sum = {total_ex1}, Average = {avg_ex1:.2f}\n")


# ------------------------------------------------------------------------------
# EXERCISE 2: Find Maximum, Minimum Values and Their Indices
# ------------------------------------------------------------------------------
"""
[PROBLEM DESCRIPTION]
Given a list of numbers, determine the maximum value, the minimum value, and the
exact 0-based index positions where these extreme values first appear.

[STEP-BY-STEP SOLUTION GUIDE & THOUGHT PROCESS]
1. Finding the Extremes:
   - The built-in max(list) scans the list and returns the highest numeric value.
   - The built-in min(list) scans the list and returns the lowest numeric value.
2. Finding the Index:
   - Calling list.index(val) locates and returns the index of the first occurrence of val.
3. Algorithmic Consideration:
   - Calling max() followed by list.index() takes two passes through the list (2 * O(n) = O(n)).
   - For an interview or large dataset, you can also solve this in a single pass by
     iterating with enumerate() and updating running max_val, max_idx, min_val, min_idx.
4. Handling Edge Cases:
   - If the list contains duplicate maximums (e.g., [85, ..., 85]), list.index() returns
     the index of the first occurrence by specification.
"""
print("--- EXERCISE 2: FIND MAX, MIN AND THEIR INDICES ---")
ex2_list = [29, 10, 85, 4, 63, 85, 7]

# Step 1: Locate maximum and minimum values
max_val = max(ex2_list)
min_val = min(ex2_list)

# Step 2: Retrieve the first occurrence index for each
max_idx = ex2_list.index(max_val)
min_idx = ex2_list.index(min_val)

# Step 3: Print findings
print(f"List: {ex2_list}")
print(f"Max: {max_val} (at index {max_idx})")
print(f"Min: {min_val} (at index {min_idx})\n")


# ------------------------------------------------------------------------------
# EXERCISE 3: Count and Separate Even and Odd Numbers
# ------------------------------------------------------------------------------
"""
[PROBLEM DESCRIPTION]
Given a list of integers, partition them into two separate lists: one containing
all even numbers and the other containing all odd numbers. Display both lists along
with their respective item counts.

[STEP-BY-STEP SOLUTION GUIDE & THOUGHT PROCESS]
1. Mathematical Condition for Parity:
   - An integer x is even if the remainder when divided by 2 is 0 (x % 2 == 0).
   - An integer x is odd if x % 2 != 0 (or x % 2 == 1).
2. Separation Strategy (List Comprehension):
   - Using list comprehensions provides an elegant, expressive, and optimized solution:
     even_nums = [x for x in list if x % 2 == 0]
     odd_nums  = [x for x in list if x % 2 != 0]
3. Alternative Strategy (Single Loop):
   - Loop through the list once. Check if item % 2 == 0; if True, append to even_nums,
     else append to odd_nums. Both approaches are O(n) in time complexity.
4. Counting:
   - Use len(even_nums) and len(odd_nums) to get the sizes of both partitioned groups.
"""
print("--- EXERCISE 3: COUNT AND SEPARATE EVEN / ODD ---")
ex3_list = [1, 4, 7, 8, 10, 13, 16, 19, 22]

# Step 1: Filter even numbers using list comprehension
even_nums = [x for x in ex3_list if x % 2 == 0]

# Step 2: Filter odd numbers using list comprehension
odd_nums = [x for x in ex3_list if x % 2 != 0]

# Step 3: Output partitioned lists and counts
print(f"Original List: {ex3_list}")
print(f"Even numbers ({len(even_nums)}): {even_nums}")
print(f"Odd numbers ({len(odd_nums)}): {odd_nums}\n")


# ------------------------------------------------------------------------------
# EXERCISE 4: Remove Duplicates While Preserving Original Order
# ------------------------------------------------------------------------------
"""
[PROBLEM DESCRIPTION]
Given a list with duplicate elements, remove all subsequent duplicates so that every
element appears only once, while strictly preserving the order of their first appearance.

[STEP-BY-STEP SOLUTION GUIDE & THOUGHT PROCESS]
1. The Trap of list(set(...)):
   - Converting to a set via list(set(ex4_list)) removes duplicates, but sets are
     inherently unordered collections based on hash values. In many Python versions or
     different data types, set conversion scrambles the original relative ordering.
2. The Recommended Approach (Collector List + Tracking Set):
   - Maintain a result list: unique_list = []
   - To make duplicate lookup fast (O(1) instead of O(n) per element), maintain an
     auxiliary set: seen = set()
   - Iterate through each item in the original list:
     * If item is not in seen:
       - Add item to seen.
       - Append item to unique_list.
3. Complexity Analysis:
   - Time Complexity: O(n) because set membership checks take O(1) average time.
   - Space Complexity: O(n) to store the auxiliary set and result list.
"""
print("--- EXERCISE 4: REMOVE DUPLICATES ---")
ex4_list = [1, 3, 2, 3, 4, 1, 5, 2, 6, 4]

# Step 1: Initialize collector list and tracking set for fast O(1) lookup
unique_list = []
seen = set()

# Step 2: Iterate and preserve insertion order
for item in ex4_list:
    if item not in seen:
        seen.add(item)
        unique_list.append(item)

# Step 3: Print result
print(f"Original List: {ex4_list}")
print(f"After Removing Duplicates: {unique_list}\n")


# ------------------------------------------------------------------------------
# EXERCISE 5: Separate Negative and Non-Negative Numbers
# ------------------------------------------------------------------------------
"""
[PROBLEM DESCRIPTION]
Given a list of positive and negative numbers (including zero), partition them into
two separate lists:
1. Negative numbers (< 0)
2. Non-negative numbers (>= 0, which includes zero and positive integers)

[STEP-BY-STEP SOLUTION GUIDE & THOUGHT PROCESS]
1. Defining the Partition Threshold:
   - In mathematics, the number 0 is neither strictly positive nor negative, but it is
     non-negative. Thus, the condition for negative is x < 0, and non-negative is x >= 0.
2. Implementation via List Comprehensions:
   - Negative:     [x for x in list if x < 0]
   - Non-negative: [x for x in list if x >= 0]
3. Order Preservation:
   - List comprehensions preserve the exact left-to-right relative order of elements
     from the original list.
"""
print("--- EXERCISE 5: SEPARATE NEGATIVE AND NON-NEGATIVE ---")
ex5_list = [-10, 15, -3, 0, 22, -8, 7, -1]

# Step 1: Filter elements strictly less than zero
negative_nums = [x for x in ex5_list if x < 0]

# Step 2: Filter elements greater than or equal to zero
non_negative_nums = [x for x in ex5_list if x >= 0]

# Step 3: Output separated results
print(f"List: {ex5_list}")
print(f"Negative numbers: {negative_nums}")
print(f"Non-negative numbers: {non_negative_nums}\n")


# ------------------------------------------------------------------------------
# EXERCISE 6: Reverse a List Manually (Without Using reverse() or [::-1])
# ------------------------------------------------------------------------------
"""
[PROBLEM DESCRIPTION]
Reverse the elements of a list using a custom manual algorithm, without relying on
built-in shortcuts such as list.reverse() or extended slicing [::-1].

[STEP-BY-STEP SOLUTION GUIDE & THOUGHT PROCESS]
There are two classical ways to solve this algorithmically:

Method A: Backward Traversal (Out-of-Place, creates new list):
1. Create an empty result list: custom_reversed = []
2. Start a loop at the last index: len(list) - 1.
3. Decrement the index step by -1 down to 0: range(len(list) - 1, -1, -1).
4. In each step, append list[i] to custom_reversed.

Method B: Two-Pointer Swap Technique (In-Place, O(1) extra space):
1. Initialize two pointer variables: left = 0, right = len(list) - 1.
2. While left < right:
   - Swap the values: list[left], list[right] = list[right], list[left]
   - Move left pointer forward: left += 1
   - Move right pointer backward: right -= 1
This in-place two-pointer technique is a fundamental algorithmic pattern in computer science.
"""
print("--- EXERCISE 6: CUSTOM LIST REVERSAL ALGORITHM ---")
ex6_list = [10, 20, 30, 40, 50]

# Method A: Backward traversal using range with negative step
custom_reversed = []
for i in range(len(ex6_list) - 1, -1, -1):
    custom_reversed.append(ex6_list[i])

print(f"Original List: {ex6_list}")
print(f"Reversed List (Method A): {custom_reversed}")

# Method B demonstration: In-place two-pointer reversal on a copy
in_place_list = ex6_list.copy()
left, right = 0, len(in_place_list) - 1
while left < right:
    # Simultaneous tuple assignment swap
    in_place_list[left], in_place_list[right] = in_place_list[right], in_place_list[left]
    left += 1
    right -= 1

print(f"Reversed List (Method B - In-Place Swapping): {in_place_list}\n")


# ------------------------------------------------------------------------------
# EXERCISE 7: Find Elements Appearing More Than k Times
# ------------------------------------------------------------------------------
"""
[PROBLEM DESCRIPTION]
Given a list of elements and a threshold integer k, identify all unique elements
whose frequency of occurrence strictly exceeds k.

[STEP-BY-STEP SOLUTION GUIDE & THOUGHT PROCESS]
1. Identifying Unique Candidates:
   - Multiple copies of the same value exist in the list. To avoid counting and printing
     the same element more than once, extract unique items first using set(list).
2. Counting Occurrences:
   - For each distinct element in the set, check its count in the original list using
     ex7_list.count(item).
   - If count > k, append item to the result list.
3. Optimization Note for Large Data:
   - Calling list.count() inside a loop is O(n * u) where u is number of unique elements.
   - For high-performance needs, count all frequencies in a single O(n) pass using a
     dictionary (or collections.Counter), then filter keys where freq > k.
"""
print("--- EXERCISE 7: FIND ELEMENTS OCCURRING > K TIMES ---")
ex7_list = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]
k = 2

# Step 1: Collect unique items where list.count() exceeds threshold k
result_ex7 = []
for item in set(ex7_list):
    if ex7_list.count(item) > k:
        result_ex7.append(item)

# Sort result for clean, deterministic presentation
result_ex7.sort()

# Step 2: Output findings
print(f"List: {ex7_list}")
print(f"Threshold k: {k}")
print(f"Elements occurring more than {k} times: {result_ex7}\n")


# ------------------------------------------------------------------------------
# EXERCISE 8: Find the Second Largest Number in a List
# ------------------------------------------------------------------------------
"""
[PROBLEM DESCRIPTION]
Find the second largest unique number in a list of numbers.

[STEP-BY-STEP SOLUTION GUIDE & THOUGHT PROCESS]
1. The Duplicate Maximum Pitfall:
   - Consider the list [15, 30, 45, 45, 20, 10].
   - If you simply sort the list ascending and select index [-2], you will get 45!
     However, 45 is the maximum, NOT the second largest value.
2. Strategy 1 (Set Deduplication + Sort):
   - Step 1: Eliminate duplicate values using set(): set(ex8_list) -> {10, 15, 20, 30, 45}.
   - Step 2: Sort the unique items in descending order: [45, 30, 20, 15, 10].
   - Step 3: The element at index 1 is guaranteed to be the strictly second largest number.
3. Strategy 2 (Single-pass Iteration - O(n)):
   - Maintain two variables: first_max = -inf, second_max = -inf.
   - For each number x:
     * If x > first_max: second_max = first_max; first_max = x
     * Else if first_max > x > second_max: second_max = x
4. Edge Case Handling:
   - If the list has fewer than 2 distinct elements (e.g., [10] or [5, 5, 5]), a second
     largest value does not exist. Always check if len(unique_sorted) > 1.
"""
print("--- EXERCISE 8: FIND SECOND LARGEST NUMBER ---")
ex8_list = [15, 30, 45, 45, 20, 10]

# Step 1: Deduplicate elements and sort in descending order
unique_sorted = sorted(list(set(ex8_list)), reverse=True)

# Step 2: Extract index 1 if at least two unique items exist
second_largest = unique_sorted[1] if len(unique_sorted) > 1 else None

# Step 3: Print result
print(f"List: {ex8_list}")
print(f"Unique values (descending): {unique_sorted}")
print(f"Second largest number: {second_largest}\n")


# ------------------------------------------------------------------------------
# EXERCISE 9: Insert x into a Sorted List to Keep it Sorted
# ------------------------------------------------------------------------------
"""
[PROBLEM DESCRIPTION]
Given a list that is already sorted in ascending order, insert a new element x into
the list at the exact position required to ensure the entire list remains sorted.

[STEP-BY-STEP SOLUTION GUIDE & THOUGHT PROCESS]
1. Understanding the Sorted Property:
   - Because the list is in ascending order, elements start small and increase.
2. Linear Scan Algorithm:
   - Iterate through each index i from 0 to len(list) - 1:
     * Check if list[i] > x.
     * The first element that is strictly greater than x indicates the exact index where
       x should be placed to preserve order.
     * Call list.insert(i, x), mark a flag inserted = True, and immediately break from loop.
3. Boundary Case (x is the new maximum):
   - If the loop finishes without inserting (meaning no element was greater than x),
     x is larger than all current items. Simply append it: list.append(x).
4. Standard Library Alternative:
   - Python's built-in module 'bisect' provides 'bisect.insort(list, x)', which uses
     binary search in O(log n) time to find the insertion index.
"""
print("--- EXERCISE 9: INSERT X INTO SORTED LIST ---")
ex9_list = [10, 20, 30, 40, 50]
x = 25

print(f"Original Sorted List: {ex9_list}")
print(f"Element to insert: x = {x}")

# Step 1: Find the first index where list element exceeds x
inserted = False
for i in range(len(ex9_list)):
    if ex9_list[i] > x:
        ex9_list.insert(i, x)
        inserted = True
        break

# Step 2: If x is greater than all existing elements, append to end
if not inserted:
    ex9_list.append(x)

# Step 3: Output final sorted list
print(f"After inserting x = {x}: {ex9_list}\n")


# ------------------------------------------------------------------------------
# EXERCISE 10: Simple Student List Management Application (Add, Remove, Search, Sort)
# ------------------------------------------------------------------------------
"""
[PROBLEM DESCRIPTION]
Build a simulated student roster management routine demonstrating core CRUD (Create,
Read, Update, Delete) operations using list methods:
1. Initialize an initial roster of student names.
2. Add a new student to the roster.
3. Safely remove an existing student.
4. Search for a student by name and locate their current seat/index position.
5. Sort the entire roster in alphabetical order (A to Z).

[STEP-BY-STEP SOLUTION GUIDE & THOUGHT PROCESS]
1. Initializing the Collection:
   - Use a list of string literals: students = ["Alice", "Bob", "Charlie", "David"]
2. Adding (Create):
   - Call students.append("Emma") to place Emma at the end of the roster.
3. Safe Deletion (Delete):
   - Calling remove("Bob") directly would crash if "Bob" wasn't present.
   - Always safeguard with membership check: if "Bob" in students: students.remove("Bob").
4. Searching (Read):
   - Use membership operator 'in' to verify presence.
   - Use students.index("Charlie") to find their zero-based position in the list.
5. In-Place Alphabetical Sorting (Update):
   - Call students.sort() to sort strings lexicographically in-place.
"""
print("--- EXERCISE 10: STUDENT LIST MANAGEMENT ---")
students = ["Alice", "Bob", "Charlie", "David"]
print(f"1. Initial student roster: {students}")

# Step 1: Add new student
students.append("Emma")
print(f"2. After adding 'Emma': {students}")

# Step 2: Safe removal of student 'Bob'
target_remove = "Bob"
if target_remove in students:
    students.remove(target_remove)
    print(f"3. After safely removing '{target_remove}': {students}")
else:
    print(f"3. Student '{target_remove}' not found for removal.")

# Step 3: Search for student 'Charlie'
search_name = "Charlie"
if search_name in students:
    pos = students.index(search_name)
    print(f"4. Found '{search_name}' at index position: {pos}")
else:
    print(f"4. '{search_name}' was not found in the roster.")

# Step 4: Sort list alphabetically (A-Z)
students.sort()
print(f"5. Final roster sorted alphabetically (A-Z): {students}\n")

print("=" * 70)
print("            ALL 10 EXERCISES COMPLETED SUCCESSFULLY!")
print("=" * 70)
