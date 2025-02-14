# Creating list from list
a = [2,3,4,5,6]
b = [value ** 2 for value in a]
print(b)

# Saving with a for loop
c = []
for value in a:
     c.append(value ** 3)
print(c)

# creating a numnber list with just range
d = [i for i in range(25)]
print(d)

# 2D matrix copy to 1D
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row ]
print(res)

# 2D matrix copy 2D
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for val in mat]
print(res)
