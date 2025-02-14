# type: ignore

# Array With list
a = [3, 'Name', 1, 2]
print(a)

# Adding in Array / List
a.append(9)
print(a)

# Numpy -----------
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

# Multiplying the whole array
print(arr * 2)

# 2D array
arr2 = np.array([[1,2],[3,4]])
print(arr2)

# Multiplying Whole array
print(arr2 * 2)


# array ---------
import array as arr

# creating array of float 'f'
a = arr.array('f', [1, 2, 3])

# accessing First Araay
print(a[0])

# Adding element to array
a.append(5)
print(a) 

# Prints only the values
print(*a)

# Inserting in array index 1 value 7
a.insert(1,7)
print(*a)

# using remove() method to remove first occurance of 1
a.remove(1)
print(*a)

# Pop() method - remove item atindex 2
a.pop(2)
print(*a)

# slicing array
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l) # passing the list in array or object referance

Sliced_array = a[3:8]
print(Sliced_array)

Sliced_array = a[5:]
print(Sliced_array)

Sliced_array = a[:]
print(Sliced_array)

# Array index number of the value 
print(a.index(1))

# Updating array
a[0] = 11
print(*a)

# ocurrrence in the array f values
print(a.count(2))


a = arr.array('i',[1,2,3,4])

# Array Expanding
a.extend([5,9,7,8,6])
print(*a)

# sorting Array
f = sorted(a)
print(*f)

# Array Reversing
a.reverse()
print(*a)

