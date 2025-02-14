import heapq

# making a heap 
li = [1,2,3,4,5,6]

heapq.heapify(li)
print(li)

# Adding to heap
heapq.heappush(li, 7)
print(li)

# Removing smallest value from the heap
min = heapq.heappop(li)
print(min)
print(li)

# Add new element to the heap then pops the smallest value, if the pushed valued is samll it will get poped
p = heapq.heappushpop(li, 9)
print(p)
print(li)

# Largest Element in Heap
maxval = heapq.nlargest(1, li)
print(maxval)

# Smallest Element in Heap
minval = heapq.nsmallest(1, li)
print(minval)

# Replacing the smallest value in the heap with the given value
heapq.heapreplace(li, 12)
print(li)

# merging a heap
h1 = [1, 2, 4]
heapq.heapify(h1)
h2 = [3, 5, 7, 4]
heapq.heapify(h2)
h3 = list(heapq.merge(h1, h2))
print(h3)

