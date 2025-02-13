# initializing 
set1 = { 1, 2, 3, 4, 5}
print(set1)

# Creating a Set
set2 = set()
print(set2)

set1 = set("GeeksForGeeks")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Geeks": 3, "for": 1, "Geeks": 2}
print(set(d))

# Adding in set 
set1.add("For2")
print(set1)

# Adding multiple
set1.update([1,"geeks"])
print(set1)

# Accessing element using For loop
for i in set1:
    print(i, end=" ")

# Checking the element# using in keyword
print("\n","Geeks" in set1)

# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  

# Using discard() Method to reemove
set1.discard(1)
print(set1)

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)

# Removing the first element in set with pop()
set1 = {1, 2, 3, 4, 5}
val = set1.pop()
print(val)
print(set1)

# Clear the set to make it empty
set1.clear()
print(set1)  

# Frozen set can not be changed after initilization

# Creating a frozenset from a list
fset = frozenset([1, 2, 3, 4, 5])
print(fset)  

# Creating a frozenset from a set
set1 = {3, 1, 4, 1, 5}
fset = frozenset(set1)
print(fset)  

# Typecasting list into set
li = [1, 2, 3, 3, 4, 5, 5, 6, 2]
set1 = set(li)
print(set1)

# Typecasting string into set
s = "GeeksforGeeks"
set1 = set(s)
print(set1)

# Typecasting dictionary into set
d = {1: "One", 2: "Two", 3: "Three"}
set1 = set(d)
print(set1)

set1 = {1, 2, 3, 4} 
 
# function to copy the set
set2 = set1.copy()
print(set2)

# Returns Unions
set1 = {1,2,3,4}
set2 = {5,2,7,8,9}
set3 = set1.union(set2)
print(set3)

# Returns difference form the other set 
set4 = set1.difference(set2)
print(set4)

set5 = set2.difference(set1)
print(set5)

# Retruns Intersection
# intersection_update  , updates and saves in the first set
set6 = set1.intersection(set2)
print(set6)

# Returns True if two sets have a null intersection
print(set1.isdisjoint(set2))

# Returns True if another set contains this set
print(set1.issubset(set2))

# Returns True if this set contains another set
print(set1.issuperset(set2))

# Returns the symmetric difference of two sets as a new set
# symmetric_difference_update() , updates it self
set7 = set1.symmetric_difference(set2)
print(set7)

# Removes all elements of another set from this set
set1.difference_update(set2)
print(set1)
