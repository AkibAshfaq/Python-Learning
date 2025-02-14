from collections import Counter

val = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Creating a Counter
ctr = Counter(val)
print(ctr)

# Strng cracter count
c = "Name"
d = Counter(c)
print(d)

# Count for specific value . works like dicionary
print(ctr[3])
print(d['N'])

# Update  -- Adds upto the list and counts again
ctr.update([2, 2, 5, 6])
print(ctr)

# From Count Dicionary to list
li = list(ctr.elements())

# ahow n amount of elements count and element in a pair from first (Empty means all elements)
# (element, count)
n = 5
com = ctr.most_common(n)
print(com)

# Subtracting Elements from list
ctr.subtract([2,1,4])
print(ctr)


# Counter combination
ctr1 = Counter([1, 2, 2, 3])
ctr2 = Counter([2, 3, 3, 4])

# Addition
print(ctr1 + ctr2)

# Subtraction
print(ctr1 - ctr2)

# Intersection
print(ctr1 & ctr2)

# Union
print(ctr1 | ctr2) 