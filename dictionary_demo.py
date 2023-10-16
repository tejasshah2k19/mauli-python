data = {
    "firstName":"ram",
    "email":"ram@gmail.com",
    "contact":9876545678,
    "alternateContact":9876545678,
    "firstName":"laxman"
}

print(data)

print(data.get("firstName"))
print(data.get("lastName"))

#keys are unique , value can be duplicate 

data.update({"email":"laxman@gmail.com"})
print(data)
#data.clear()
#del data 

len(data) #total key count

print(data["firstName"])
data.pop("firstName")
print(data)
print(data.values())
print(data.keys())
data.popitem()#remove the last added item 
print(data)
