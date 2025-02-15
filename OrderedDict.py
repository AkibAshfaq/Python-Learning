from collections import OrderedDict


# Creating order dictionay
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)


# Update adds on the last of position on the dictionary
od['a'] = 0
print(od)

od1 = od
# Compare 
print(od1 == od)

# recversing the dictonary
r_od = OrderedDict(reversed(list(od.items())))
print(r_od)

# Poping firdt item
lastitem = r_od.popitem(last=False)
print(r_od)

# Poping last item
firstitem = r_od.popitem(last=True)
print(r_od)

# Relocating elements at last position
r_od.move_to_end('c')
print(r_od)

# Reloactiong the elemants at first location
r_od.move_to_end('b', last = False)
print(r_od)

# Updating by function adds at last 
r_od.update([('e', 2), ('f', 3)])
print(r_od)

