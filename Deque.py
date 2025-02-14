from collections import deque

# Creating deque
de = deque([1,2,3,4,5])
print(de)       # deque([1, 2, 3, 4, 5])

# Add to the right end of the deque
de.append(6)
print(de)       #OUTPUT : deque([1, 2, 3, 4, 5, 6])

# Add on left 
de.appendleft(0)
print(de)       #OUTPUT :  deque([0, 1, 2, 3, 4, 5, 6])

# remove from right
de.pop()
print(de)       #OUTPUT :  deque([0, 1, 2, 3, 4, 5])

# remove from left
de.popleft()
print(de)       #OUTPUT :  deque([1, 2, 3, 4, 5])

# Extend right
de.extend([6,7,8])
print(de)       #OUTPUT :  deque([1, 2, 3, 4, 5, 6, 7, 8])

# Extend left
de.extendleft([-1,0])
print(de)       #OUTPUT :  deque([0, -1, 1, 2, 3, 4, 5, 6, 7, 8])

# remove first ocurrence from deque
de.remove(-1)
print(de)       #OUTPUT :  deque([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Rotate the deque n steps
de.rotate(3)
print(de)       #OUTPUT :  deque([6, 7, 8, 0, 1, 2, 3, 4, 5])

# Count
print(de.count(1))      #OUTPUT :  1

# index of the first occured value
print(de.index(1))      #OUTPUT :  4

# Reverse
de.reverse()
print(de)               #OUTPUT :  deque([5, 4, 3, 2, 1, 0, 8, 7, 6])

# Accessing value
print(de[1])            #OUTPUT :  4

# length
print(len(de))          #OUTPUT :  9

# Clear Deque
de.clear()
print(de)               #OUTPUT :  deque([])




