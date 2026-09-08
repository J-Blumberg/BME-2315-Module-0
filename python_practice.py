# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
Set value of X euqal to zero
Set value of 1st variable A equal to zero
Set value of second variable B equal to 1
Set value of total T equal to zero

Check if N is greater than X:

Add A to T

Set variable C = A + B
Set A = B
Set B = C
Add 1 to X

Repeat until X = N
"""



# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 #Number we are comparing to N
total = 0 #Total value of numbers in seqeunce less than N

while count < N:
    total = total + a #adding lowest current fibonacci number to total

    next_value = a + b #getting next value in seqeuence by adding a+b
    a = b #setting a equal to b to continue the series
    b = next_value #setting b equal to next value to continue the series

    count = count + 1

print(total)

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.
import numpy as np #Importing NumPy
fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] #Create the list of numbers
standard_deviation = np.std(fib_numbers) #Set out variable equal to standard deviation of the list of numbers 
print(standard_deviation) #display the standrd deviation or in other words display the varible we just created

'''
Used Chat GPT for two things in this problem.
- 1st on how to import NumPy and the syntax needed for that. 
- How to create a list and the syntax needed for the standard deviation function np.std()

'''

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.
'''
Under the function is the same code that was used for Problem 2
'''



def sum_fibonacci(N): #defines the function
    a = 0
    b = 1
    total = 0

    for count in range(N): # Repeat exactly N times
        total = total + a # Add the current fibonacci number
        next_value = a + b
        a = b #set a equal to previous numbers 
        b = next_value #move to the next number

    return total  # Send the sum back to wherever the function was called

results = [] #creates a list to store the sums calculated

for N in [5, 10, 15, 20, 25, 30]: #Creates a list to go through each value of N listed
    results.append(sum_fibonacci(N)) #calculates the sum of N and adds it to the list

print(results) #displays the list



# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.




def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 #Type error
    b = 1 #Type error
    index = 0 #UnboundLocalError

    while a <= limit: #Type error both and b need to get the quotes removed around them 
        next_value = a + b
        a = b
        b = next_value
        index += 1 #Unbound Local Error: This is because index does not have a starting value so need to set index equal to zero before loop

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_odd_fib(limit): #renamed to odd
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 != 0:  # Selects odd numbers
            total += b # Adds to our total instead of repating it
        a, b = b, a + b
    return total


# Add your test cases here
print(sum_odd_fib(10))
test_cases = [
    (0, 0),    # No positive Fibonacci numbers included
    (1, 2),    # Includes both occurrences of 1
    (2, 2),    # The even number 2 should not change the sum

]
for limit, expected in test_cases:
    actual = sum_odd_fib(limit)
    print("Limit:", limit, "Expected:", expected, "Actual:", actual)
    assert actual == expected  # Raises an AssertionError if a test fails

'''
Used ChatGPT to help me brainstorm tests and how to inlcude sytaxt at the end to display the tests.
'''
# %%
