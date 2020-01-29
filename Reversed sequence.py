Get the number n (n>0) to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]

# create a new array
# loop through the array
# append method adds last element to the array and return the new reversed array
def reverse_seq(n):
    pass
    reverse_n = []
    for i in range(n):
        reverse_n.append(n - i)
    return reverse_n
