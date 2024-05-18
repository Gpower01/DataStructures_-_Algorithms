"""
O(n^2) Time Complexity 

: Nested Loops: The outer loop iterates over each element, and the inner loop checks the rest of the elements for duplicates.

:Range Adjustment: The inner loop starts from i + 1 to avoid comparing the same element with itself.

:String Formatting: Using an f-string to correctly format the output.

:Break Statement: The break statement exits the inner loop when a duplicate is found.

NOTE:
: However, this solution is still O(n^2) in time complexity. To improve efficiency, you can use a `set` to track duplicates in O(n) time:
"""
import time

numbers = [3, 6, 2, 4, 3, 6, 8, 9]

# Original O(n^2) solution
start = time.time()

# Finding duplicates
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(f"{numbers[i]} is a duplicate")
            break

original_finish = time.time()
original_time_delta = original_finish - start


# Optimized O(n) solution
"""
: Using a Set: The seen set keeps track of numbers that have been encountered.

:Single Loop: Iterate over each number and check if its in the seen set.

:Efficient Check: Checking membership and adding to a set both have average time complexity of O(1).

:Output: Print the number if its already in the set, otherwise add it to the set.

NOTE:
This optimized solution is more efficient and has a time complexity of O(n).
"""

numbers = [3, 6, 2, 4, 3, 6, 8, 9]
seen = set()

# Start the timer
start = time.time()

# Finding duplicates
for number in numbers:
    if number in seen:
        print(f"{number} is a duplicate")
    else:
        seen.add(number)

optimized_finish = time.time()
optimized_time_delta = optimized_finish - start

# Print the time taken for both solutions
print(f"Time taken for the original O(n^2) solution: {original_time_delta} seconds")
print(f"Time taken for the optimized O(n) solution: {optimized_time_delta} seconds")
print(f"Time difference: {original_time_delta - optimized_time_delta} seconds")