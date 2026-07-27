# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

n=int(input("How many numbers? "))
numbers=[]
for i in range(1,n+1):
        if i <= n:
            number=int(input("Enter number" +str(i)+": "))
            numbers.append(number)
            i=i+1
print("Results:")
def the_sum(numbers):
    sum=0
    for number in numbers:
        sum+= number
    return sum
def the_average(numbers):
    return the_sum(numbers)/n
def the_maximum(numbers):
    maximum=numbers[0]
    for num in numbers:
        if num>maximum:
            maximum=num
    return maximum
def the_minimum(numbers):
    minimum=numbers[0]
    for number in numbers:
        if number<minimum:
            minimum=number
    return minimum
print("Sum: "+str(the_sum(numbers)))
print("Average: "+str(the_average(numbers)))
print("Maximum: "+str(the_maximum(numbers)))
print("Minimum: "+str(the_minimum(numbers)))







