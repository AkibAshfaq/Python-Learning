# Intializing Tuple
a = (5, 'Akib')
print(a)

# Nested Tuple 
b1 = (0, 1, 2, 3)
b2 = ('people 1', 'people 2')
b = ( b1, b2)
print(b)

# Tuple Repettion
c = ('A') * 3
print(c)

# Accesssing Tuple with indexing
d = ("Akib")
print (d[1])

# Accessign with range
print(d[1:4])
print(d[:2])


# Tuple Unpacking
a, b, c, d = b1

print(a)
print(b)
print(c)
print(d)

# Concatination of Tuple
b1 = (0, 1, 2, 3)
b2 = ('people 1', 'people 2')
b = b1 + b2
print(b) 

# Slicing of a Tuple with Numbers
tup = tuple('GEEKSFORGEEKS')

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])

# Dleleing Tuple
del tup

# Reinitializing
tup = tuple('GEEKSFORGEEKS')

# Return Location 
print(tup.index('E'))

# Counts 
print(tup.count('E'))

# Returns if all true
print(all(tup))

# Return if any
print(any(tup))

# Return length
print(len(tup))

# Saved location 
print(enumerate(tup))

# maximum Number
print(max(tup))

# Minimum Number
print(min(tup))

# Returns summation 
s = (5, 2, 3, 4, 1)
print(sum(s))

# Return Sorted Tuple
print(sorted(s))
