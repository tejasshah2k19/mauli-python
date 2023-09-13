x ="     royal    "
print(x)
print(len(x))
print(x.strip())
print(len(x.strip()))
print(x.lstrip())
print(x.rstrip())


x = "#####royal######"
print(x.strip("#"))
print(x.lstrip("#"))
print(x.rstrip("#"))

print(x)# immutablity 

x  = x.strip("#")
