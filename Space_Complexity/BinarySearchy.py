"""
Let's take this simple example where we want to search for number 68 with an O(n) complecity
In this simple example, we have a very small numbers to search through - so the programme will run very fast.

However, let's assume we have a billion number to search through, we don't want to iterate through a billion number because - it will take forever 
: This is where Binary Search comes into play
"""
numbers = [4, 9, 15, 21, 34, 57, 68, 91]

for i in range(len(numbers)):
    if numbers[i] == 68:
        print(i)

"""
Binary Search: iteration k = n/2^k
: For k iterations 

Big O notation: O(log n)
 
n/2 (iteration 1): We first find the middle number (which is 21) and compare it to 68 --n/2
And since 21 is less than 68, we will discard the arrays in the left

(n/2)/2 = n/2^2 (iteration 2): So now we are only left with [34, 57, 68, 91] - and here the middle array is 57 - hence we will discarc the left side array [34, 57]

(n/2^2)/2 = n/2^3 (iteration 3): We are now left with [68, 91] in our search space 

Again we divide it by and take the middle number which is 68 - the right answer

:So for this example we have 8 elements - applying Big O notation O(log n) -> log2 8 -> log2  2^3 -> 3* log2 2 = 3 (iterations)
"""