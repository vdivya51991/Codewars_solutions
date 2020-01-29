# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

# create a temp variable
# iterate through each variable in the array and square it
# add all the squared values and return the result

def square_sum(numbers):
    total = 0;
    for i in numbers:
      total += i * i
    return total
