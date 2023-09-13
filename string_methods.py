str = "royAl edUcation"

print(str)
print(str.capitalize())
print(str.title())
print(str.upper())
print(str.lower())

print(str.count("@"))
print(str.count("o"))

#google 
email = "rock@gmail.com"

print(email.endswith("@gmail.com")) # True False 
print(str.startswith("Royal")) #True False

print(email.index("@"))

#signup 
name = "ram123"
print(name.isalpha()) # check all data in string must be alphabet True False 
mobile = "9856256245"
print(mobile.isdigit())
#islower isupper isalnum isprintable isspace 


#strip lstrip rstrip 

str = "royal education ahmedabad"
print(str.replace("education","technosoft"))


print(str.replace("a","A"))


str = "jony jony yes papa"

print(str.count("jony"))

words = str.split(" ")

print(words)
print(words[0])

for x in words:
    print(x)





