# Initialize empty list
a = []

# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20 ,30])  
print("After extend([15, 20, 30]):", a)

# Removing the specific element in list
a.remove(20)
print("After removing 20 in list:", a)

# Removing the last element
a.pop()
print("After removing the last element", a)

# Removing the element at given index 
a.pop(1)
print("After removing the last element", a)

# Delete a specific value in index
del a[0]
print("After deleting the index 0", a)

print(a[0])

print("\nNew list in use")

# Initializing list with value
b = [10, 20, 30]

# Iterating in the list 
for i in b:
    print(i)

# 2D List
c = [
    [1,2,3], [4,5,6], [7,8,9]
]

print(c[1][2])

