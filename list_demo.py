list  = [11,21,31,41,51,21,-1,-2,33,3]

print(list.count(11)) # 1 
#list.remove(12) # error throw 
list.remove(21) # will remove single item , which occur first 
print(list)

if list.count(12) != 0:
    list.remove(12)
else:
    print("Num not present")

print("before pop", list)
list.pop() # this will remove last item from list 
print("after pop",list)
list.pop(0)
print("after pop 0 ",list)
#list.clear() 
#del list 


# print(list.index(9))

print(list.index(31))
list.sort()
print(list)
list.reverse()
print(list)

list.insert(2,2000)
print(list)