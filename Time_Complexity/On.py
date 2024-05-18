def get_squared_numbers(numbers):
    """
    Returns a list of squared numbers.
    Time complexity is O(n).

    Here the time it takes for computation is equal to the number of `n`
    So as `n` grows, the computation time grows linearly 
    """
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n * n)
    return squared_numbers

# Example 
numbers  = [2, 5, 8, 9]
res = get_squared_numbers(numbers)
print(res)  # Output: [4, 25, 64, 81]

# Another example of a time constant
