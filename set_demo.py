x = {}

a = {1,2,3,4,5,6,7}
b = {1,3,4,6,8}

c = a.union(b)
print(c)
print(a)
print(b)

#a.update(b) #a.union_with_update(b) => a U b => a 

c = a.intersection(b)
print(c)
print(a)
print(b)

# a.intersection_update(b) #

#a.clear()
print(len(a))

print(a.difference(b)) #a - b 

# a.difference_update(b)
a.discard(99)
a.discard(7)
print(a)
# a.remove(99)
a.pop()
# a.pop(1)

print(a)
 
a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)

a = {1,2,3,4,5,6,7}
b = {1,3,4,6,8}
print(a.symmetric_difference(b)) # a-b U b-a  {2 5 7 } {8 } 